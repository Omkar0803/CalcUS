import os
import subprocess
import shlex

if not os.path.isdir("/binaries/xtb/xtb"):
    subprocess.call(shlex.split("tar xvfj xtb_suite.tar.bz2"), cwd="/binaries/xtb/")
    subprocess.call(
        shlex.split("chmod +x crest stda xtb4stda xtb/bin/xtb"), cwd="/binaries/xtb/"
    )
