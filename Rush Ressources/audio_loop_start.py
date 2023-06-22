# by me

import pygame

async def audio_loop_start():
    global is_audio_playing, is_audio_looping

    if is_audio_playing:
        pygame.mixer.music.play(-1)
        is_audio_looping = True
        print("Audio looping started.")
    else:
        print("No audio is currently playing.")

asyncio.run(audio_loop_start())
