#by me lmfao

import subprocess

def hide_check():
    print("Checking if console is hidden...")
    console_visible = True
    if subprocess.STARTUPINFO().dwFlags & subprocess.STARTF_USESHOWWINDOW:
        console_visible = False
    if console_visible:
        print("```False```")
    else:
        print("```True```")

hide_check()
