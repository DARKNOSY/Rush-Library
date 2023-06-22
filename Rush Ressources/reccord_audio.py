# by me

import sounddevice as sd

async def record_audio(duration: int):
    print(f"Started recording audio for {duration} minutes.")
    audio_frames = sd.rec(duration * 60 * 44100, samplerate=44100, channels=2)
    sd.wait()
    sd.write('audio_recording.wav', audio_frames, samplerate=44100)
    print("Audio recording finished.")

await asyncio.gather(record_audio(5))
