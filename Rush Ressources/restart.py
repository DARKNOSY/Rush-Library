# by me

import os

if os.name == "nt":
    import ctypes

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
else:
    def is_admin():
        return os.getuid() == 0

if is_admin():
    os.system("shutdown /r /t 0")
    print("Restarting the computer.")
else:
    print("You need to be an admin to do this!")
