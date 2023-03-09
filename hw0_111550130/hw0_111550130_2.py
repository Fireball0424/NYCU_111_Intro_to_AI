# library
import cv2 as cv 
import numpy as np 

# read the video
cap = cv.VideoCapture('video.mp4')
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# save last frame
tmp = None

while cap.isOpened():
    ret, input = cap.read()
    if ret == False :
        break 

    # convert to gray & blur
    gray_frame = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
    blur_frame = cv.GaussianBlur(gray_frame, (5, 5), 0)

    # absdiff
    if(tmp is None):
        tmp = blur_frame
        continue
    diff = cv.absdiff(blur_frame, tmp)
    tmp = blur_frame

    # Convert to green
    result = cv.cvtColor(diff, cv.COLOR_GRAY2BGR)
    lower = np.array([0, 0, 0])
    upper = np.array([50, 50, 50])
    mask = cv.inRange(result, lower, upper)
    result[mask == 0] = [0, 255, 0]

    # show the result
    combine = np.hstack((input, result))
    cv.namedWindow("result", cv.WINDOW_NORMAL)
    combine = cv.resize(combine, (width, height))
    cv.imshow("result", combine)
        
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()   