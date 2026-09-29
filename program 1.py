import cv2

# Open video file
video = cv2.VideoCapture("myvideo.mp4")

if not video.isOpened():
    print("Error: Unable to open video.")

else:
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv2.CAP_PROP_FPS)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

    print("Video Width :", width)
    print("Video Height:", height)
    print("Frames Per Second (FPS):", fps)
    print("Total Frames:", frames)

    video.release()