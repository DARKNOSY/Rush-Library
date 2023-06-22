# by me

import ctypes

async def show_error_box(session: str, message: str):
    full_message = f"I {message}"
    ctypes.windll.user32.MessageBoxW(None, full_message, "Error", 0)
    print(f"Error box displayed for session '{session}'.")

await asyncio.gather(show_error_box("Session1", "encountered an error"))
