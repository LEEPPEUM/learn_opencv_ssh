import cv2 as cv
import numpy as np

img = cv.imread('datas/images/lena.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayToBGR = cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)  # without Error dimension

imgHor = np.hstack((grayToBGR,img))
cv.imshow("Horizontal",imgHor)

imgVer = np.vstack((grayToBGR,img))
cv.imshow("Vertical",imgVer)

cv.waitKey(0)
cv.destroyAllWindows()