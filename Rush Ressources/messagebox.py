#adapted by me

import ctypes

def show_message_box(title, message):
    try:
        Message_box = ctypes.windll.user32.MessageBoxW
        Message_box(None, message, title, 0)
    except Exception as e:
        print("An error occurred while displaying the message box:")
        print(str(e))

title = input("Enter the title of the message box: ")
message = input("Enter the message: ")
show_message_box(title, message)
