#!/usr/bin/python3

import subprocess
import os

dirs = [d for d in os.listdir('.') if os.path.isdir(d)]

for path in dirs:
    print("Processing directory", dir)
    try:
        return_code = subprocess.call("cd ./%s/slides && make slides" % path, shell=True)
        if return_code == 0:
            print("OK")
        else:
            print("Finished with non-zero status:", return_code)
    except OSError as e:
        print("ERROR executing process:", str(e))
