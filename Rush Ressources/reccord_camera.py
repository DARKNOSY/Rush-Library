# by me

import cv2

async def record_camera(duration: int):
    video_capture = cv2.VideoCapture(0)
    frames = []
    start_time = asyncio.get_running_loop().time()
    while (asyncio.get_running_loop().time() - start_time) / 60 < duration:
        ret, frame = video_capture.read()
        if not ret:
            break
        frames.append(frame)
    height, width, _ = frames[0].shape
    video_writer = cv2.VideoWriter('camera_recording.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
    for frame in frames:
        video_writer.write(frame)
    video_writer.release()
    video_capture.release()
    print("Finished recording camera.")

await asyncio.gather(record_camera(5))
