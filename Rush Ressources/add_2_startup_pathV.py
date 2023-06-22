# adapted by me

import os
import shutil

def add_to_startup():
    try:
        if is_admin():
            startup_dir = os.path.join(
                os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            )
            file_name = __file__.split("\\")[-1]
            shutil.copyfile(__file__, os.path.join(startup_dir, file_name))
            print("Added to startup!")
        else:
            print("You need to be an admin to do this!")
    except Exception as e:
        print("An error occurred while adding to startup:")
        print(str(e))

add_to_startup()
