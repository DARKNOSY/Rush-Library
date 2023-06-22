# by me

import cv2
import os

def take_webcam_picture():
    capture = cv2.VideoCapture(0)
    
    if not capture.isOpened():
        print("Failed to open webcam")
        return
    
    ret, frame = capture.read()
    
    if not ret:
        print("Failed to capture frame from webcam")
        return
    
    capture.release()
    cv2.destroyAllWindows()
    
    return frame

def webcam_pic():
    try:
        frame = take_webcam_picture()
        if frame is not None:
            output_file = 'webcam_picture.jpg'
            cv2.imwrite(output_file, frame)
            print("Webcam picture saved:", output_file)
          # insert send file script or something
            os.system("del webcam_picture.jpg")
    except Exception as e:
        print("An error occurred while capturing a webcam picture:")
        print(str(e))

webcam_pic()
