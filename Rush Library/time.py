# by me

from datetime import datetime

def get_current_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_datetime

current_datetime = get_current_datetime()
print(f"The current date and time is: {current_datetime}")
