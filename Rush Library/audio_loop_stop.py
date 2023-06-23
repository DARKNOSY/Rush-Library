# by me

import pygame

async def audio_loop_stop():
    global is_audio_looping

    if is_audio_looping:
        pygame.mixer.music.stop()
        is_audio_looping = False
        print("Audio looping stopped.")
    else:
        print("Audio looping is not currently active.")

asyncio.run(audio_loop_stop())
