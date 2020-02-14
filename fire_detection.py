import numpy as np
import cv2

 
# video_file = "video_1.mp4"
video = cv2.VideoCapture(0)
#img = cv2.imread('fireimage.jpeg', cv2.IMREAD_GRAYSCALE)

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break
 
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.asarray(lower, dtype="uint8")
    upper = np.asarray(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)
    
 
 
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    no_red = cv2.countNonZero(mask)
    cv2.imshow("output", output)

    if int(no_red) > 20000:
        print('Fire detected')
    #print(int(no_red))
   #print("output:".format(mask))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()
video.release()
