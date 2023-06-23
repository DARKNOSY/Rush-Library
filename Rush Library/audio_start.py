# by me

import pygame
import asyncio

async def audio_start():
    global is_audio_playing
    if len(ctx.message.attachments) == 0:
        print("Please attach an audio file to play.")
        return
    audio_file = ctx.message.attachments[0]
    if not audio_file.filename.lower().endswith(('.mp3', '.wav', '.ogg')):
        print("Please attach a valid audio file (MP3, WAV, or OGG).")
        return
    file_path = f"./{audio_file.filename}"
    await audio_file.save(file_path)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    is_audio_playing = True
    print("Playing audio...")
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(1)
    is_audio_playing = False

asyncio.run(audio_start())
