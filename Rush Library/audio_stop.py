# by me

import pygame

async def audio_stop():
    global is_audio_playing
    if is_audio_playing:
        pygame.mixer.music.stop()
        is_audio_playing = False
        print("Audio playback stopped.")
    else:
        print("No audio is currently playing.")

asyncio.run(audio_stop())
