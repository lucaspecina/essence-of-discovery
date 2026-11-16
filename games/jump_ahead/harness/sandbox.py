"""La computadora chica de la IA: corre su código Python encerrado y con tope de tiempo.

Qué puede hacer el código de la IA: leer y escribir en su carpeta de trabajo, usar Python y numpy.
Qué NO puede (lo impide `sandbox-exec` de macOS): usar la red, leer archivos de la carpeta del usuario
(ahí están el repo con las respuestas y las claves), escribir fuera de su carpeta, lanzar otros programas.
Tampoco recibe variables de entorno nuestras.
"""
from __future__ import annotations

import os
import signal
import subprocess
import tempfile
import threading
import time
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SANDBOX_PYTHON = REPO / ".venv-sandbox" / "bin" / "python"
OUTPUT_CAP = 6000            # caracteres de salida que vuelven al modelo por ejecución
MEMORY_CAP_KB = 6_000_000    # si el proceso pasa de ~6 GB, se corta

PROFILE = """(version 1)
(allow default)
(deny network*)
(deny file-read-data (subpath "/Users"))
(allow file-read-data (subpath "{venv}") (subpath "{python_root}") (subpath "{workdir}"))
(deny file-write*)
(allow file-write* (subpath "{workdir}") (literal "/dev/null") (literal "/dev/dtracehelper"))
(deny process-exec*)
(allow process-exec (literal "{python_real}") (literal "{python_link}"))
"""


@dataclass
class RunResult:
    output: str
    seconds: float
    timed_out: bool
    killed_for_memory: bool
    returncode: int | None


class Sandbox:
    def __init__(self, files: dict, max_runs: int = 12, run_seconds: float = 30.0):
        self.workdir = Path(os.path.realpath(tempfile.mkdtemp(prefix="jump-ahead-")))
        for name, content in files.items():
            (self.workdir / name).write_text(content)
        self.max_runs, self.run_seconds = max_runs, run_seconds
        self.runs: list = []
        python_real = Path(os.path.realpath(SANDBOX_PYTHON))
        self._profile = self.workdir.parent / (self.workdir.name + ".sb")
        self._profile.write_text(PROFILE.format(
            venv=os.path.realpath(REPO / ".venv-sandbox"), python_root=python_real.parents[1],
            workdir=self.workdir, python_real=python_real, python_link=SANDBOX_PYTHON))

    @property
    def runs_left(self) -> int:
        return self.max_runs - len(self.runs)

    @property
    def cpu_seconds(self) -> float:
        return sum(r.seconds for r in self.runs)

    def run(self, code: str) -> RunResult:
        if self.runs_left <= 0:
            return RunResult("No quedan ejecuciones.", 0.0, False, False, None)
        script = self.workdir / f"cell_{len(self.runs) + 1}.py"
        script.write_text(code)
        env = {"PATH": "/usr/bin:/bin", "HOME": str(self.workdir), "TMPDIR": str(self.workdir),
               "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1",
               "MKL_NUM_THREADS": "1", "PYTHONDONTWRITEBYTECODE": "1", "MPLBACKEND": "Agg",
               "PYTHONUNBUFFERED": "1"}
        t0 = time.perf_counter()
        proc = subprocess.Popen(
            ["/usr/bin/sandbox-exec", "-f", str(self._profile), str(SANDBOX_PYTHON), "-s", "-E", "-B", script.name],
            cwd=self.workdir, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            errors="replace", start_new_session=True)
        flags = {"memory": False}

        def watch_memory():
            while proc.poll() is None:
                try:
                    rss = subprocess.run(["/bin/ps", "-o", "rss=", "-p", str(proc.pid)], capture_output=True, text=True)
                    if rss.stdout.strip() and int(rss.stdout.split()[0]) > MEMORY_CAP_KB:
                        flags["memory"] = True
                        os.killpg(proc.pid, signal.SIGKILL)
                        return
                except (ValueError, ProcessLookupError, OSError):
                    pass
                time.sleep(0.5)

        threading.Thread(target=watch_memory, daemon=True).start()
        timed_out = False
        try:
            out, _ = proc.communicate(timeout=self.run_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            out, _ = proc.communicate()
        seconds = time.perf_counter() - t0
        out = out or ""
        if len(out) > OUTPUT_CAP:
            out = out[: OUTPUT_CAP * 2 // 3] + f"\n... [salida recortada: {len(out)} caracteres en total] ...\n" + out[-OUTPUT_CAP // 3:]
        if timed_out:
            out += f"\n[CORTADO: pasó el límite de {self.run_seconds:.0f} segundos]"
        if flags["memory"]:
            out += "\n[CORTADO: usó demasiada memoria]"
        result = RunResult(out, seconds, timed_out, flags["memory"], proc.returncode)
        self.runs.append(result)
        return result
