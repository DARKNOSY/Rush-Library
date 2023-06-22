# by me

import pyperclip

def clipboard():
    try:
        clipboard_content = pyperclip.paste()
        print("Clipboard content:", clipboard_content)
    except Exception as e:
        print("An error occurred while accessing the clipboard:")
        print(str(e))

clipboard()
