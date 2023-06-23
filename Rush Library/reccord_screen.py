# by me

from datetime import datetime, timedelta
import asyncio
import cv2
import numpy as np
from PIL import ImageGrab

async def record_screen(duration_minutes: int):
    print("Recording started")

    start = datetime.now()
    duration = timedelta(minutes=duration_minutes)
    frames = []

    while datetime.now() - start < duration:
        img = ImageGrab.grab()
        frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

        await asyncio.sleep(0.1)

    height, width, _ = frames[0].shape
    output_file = "screen_recording.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, 10, (width, height))

    for frame in frames:
        video_writer.write(frame)
    video_writer.release()

    print("Recording completed")

await asyncio.gather(record_screen(5))
