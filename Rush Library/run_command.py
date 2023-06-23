# modified by me

import os
import io

def run_command(command):
    print("Running command...")
    output = os.popen(command).read()
    if len(output) > 2000 or "```" in output:
        with open("output.txt", "w") as file:
            file.write(output)
        print(f"Output was too long or contained a code block, so it was saved to 'output.txt'.")
    else:
        print(f"Command output:\n{output}")

command = input("Enter the command to run: ")
run_command(command)
