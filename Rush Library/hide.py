#not by me

import os
import subprocess
import sys

def hide():
    print("Hiding window... This has to make a new process so it might take a second.")
    subprocess.Popen([sys.executable, __file__], creationflags=subprocess.CREATE_NO_WINDOW)
    os._exit(0)

hide()
