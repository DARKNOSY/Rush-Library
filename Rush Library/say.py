#adapted by me

import win32com.client as wincl

def speak_message(message):
    try:
        talk = wincl.Dispatch("SAPI.SpVoice")
        talk.Speak(message)
    except Exception as e:
        print("An error occurred while speaking the message:")
        print(str(e))

message = input("Enter the message to speak: ")
speak_message(message)
print(f"Said: {message}")
