from .counter3 import from_static_image
import cv2


def getCount():
    video = cv2.VideoCapture("stream/video3.mp4")
    i = 0
    while (video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            break
        if i % 30 != 0:
            i += 1
            continue

        with open("stream/count3", "w") as f:
            f.write(str(from_static_image(frame)))
        i += 1

    video.release()


if __name__ == "__main__":
    getCount()
