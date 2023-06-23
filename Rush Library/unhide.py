#not from me

import os
import subprocess
import sys

def unhide():
    print("Showing window... This has to make a new process so it might take a second.")
    subprocess.Popen([sys.executable, __file__])
    os._exit(0)

unhide()
