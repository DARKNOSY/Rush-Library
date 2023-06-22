# by me

import psutil

def kill_process_by_name(process_name):
    processes = [proc for proc in psutil.process_iter(['name']) if proc.info['name'] == process_name]
    if processes:
        for proc in processes:
            proc.kill()
        print(f"Process '{process_name}' killed successfully.")
    else:
        print(f"No process with the name '{process_name}' found.")

process_name = "example_process.exe"
kill_process_by_name(process_name)
