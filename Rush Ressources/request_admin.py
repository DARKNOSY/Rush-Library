#not from me

import ctypes
import sys

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

def ask_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        print("Asked for admin!")
    else:
        print("Already admin")

ask_admin()
