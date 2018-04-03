import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    (h, w) = frame.shape[:2]
    center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    frame = cv2.warpAffine(frame, M, (w,h))

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
