import cv2, sys
import time

if sys.platform == "win32":
    import os, msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

cap = cv2.VideoCapture(0)
while True :
    ret, frm = cap.read()
    sys.stdout.write( frm.tostring() )

# ffserver -f /etc/ffserver.conf & python stream_test.py | ffmpeg -s 640x480 -f rawvideo -pix_fmt bgr24 -r 30 -i - http://localhost/webcam.ffm
