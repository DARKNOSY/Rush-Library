#not by me

import ctypes

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

def admin_check():
    print("Checking if admin...")
    print("```" + str(is_admin()) + "```")

admin_check()
