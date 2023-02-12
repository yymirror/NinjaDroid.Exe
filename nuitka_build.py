from codecs import ignore_errors
import os
from shutil import which, rmtree
from subprocess import Popen, STDOUT
from multiprocessing import cpu_count

__NUITKA_EXEC_PATH: str = which("nuitka3")

ARGS: list = [
    __NUITKA_EXEC_PATH,
    f'--jobs={cpu_count()}',
    '--clang', '--lto=yes',
    '--disable-ccache', '--follow-imports',
    '--include-data-dir=./ninjadroid/bin64=ninjadroid/bin64',
    '--include-data-dir=./ninjadroid/config=ninjadroid/config',
    '--include-data-dir=./pyaxmlparser.resources=pyaxmlparser/resources',
    '--windows-icon-from-ico=./ninjadroid.ico',
    '--standalone', './ninjadroid',
]

GENERATED_DIRS: list = [
    './ninjadroid.build',
    './ninjadroid.dist',
]

def remove_generated():
    for dent in GENERATED_DIRS:
        rmtree(dent, ignore_errors=True)


if __name__ == '__main__':
    remove_generated()
    proc = Popen(ARGS, bufsize=0, stderr=STDOUT, shell=True)
    os._exit(proc.wait())

