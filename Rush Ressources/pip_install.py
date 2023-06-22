# by me

import subprocess

def pip_install(package_name):
    try:
        command = f'py -m pip install --upgrade {package_name}'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            output = stderr.decode()
        else:
            output = stdout.decode()

        return output
    except Exception as e:
        return f'An error occurred: {str(e)}'

package_name = "package_name"
output = pip_install(package_name)
print(output)
