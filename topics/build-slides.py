#!/usr/bin/python3

import os
import shutil
import subprocess
import sys

dirs = [d for d in os.listdir('.') if os.path.isdir(d)]


try:
    if os.path.exists("../build"):
        print("NOTE: going to remove ../build (the old build directory)")
        shutil.rmtree("../build")
    os.makedirs("../build")
except OSError as e:
    print("ERROR: Failed to remove/recreate the '../build' directory")
    sys.exit(1)

for topic in dirs:
    print("Processing directory", topic)
    try:
        return_code = subprocess.call("cd ./%s/slides && make slides" % topic, shell=True)
        if return_code == 0:
            print("OK")
        else:
            print("Finished with non-zero status:", return_code)
            continue;
    except OSError as e:
        print("ERROR running a subprocess when building slides:", str(e))

    try:
        shutil.move("./%s/slides/build/slides" % topic, "../build/%s" % topic)
    except Exception as e:
        print("ERROR: failed to move built slides to the build directory:", str(e))
        sys.exit(2)
