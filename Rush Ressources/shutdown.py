# by me

import os
import asyncio

def shutdown(message=None):
    try:
        if message is None:
            raise ValueError("Message is required.")
        
        print("Shutting down...")
        asyncio.run(async_shutdown(message))
    except ValueError as ve:
        print("Error: " + str(ve))
    except Exception as e:
        print("An error occurred while shutting down:")
        print(str(e))

async def async_shutdown(message):
    await asyncio.sleep(2)
    os.system(f'shutdown /s /t 0 /c "{message}"')

# example > shutdown("Shutting down the system now.")
shutdown("MESSAGE HERE")
