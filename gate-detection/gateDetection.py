#shape and color detection

#Credle notes

# This code uses trackbars using HSV to isolate a single color. It then detects sides of the shape.
# Future development will have it find shapes with 4 sides, our gate, and mark the center.
# Written with help from Pysource on Youtube.



#code

import cv2

import numpy as np

def nothing(x):
	pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H", "Trackbars", 21, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 36, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 94, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 58, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 168, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)


while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	l_h = cv2.getTrackbarPos("L-H", "Trackbars")
	l_s = cv2.getTrackbarPos("L-S", "Trackbars")
	l_v = cv2.getTrackbarPos("L-V", "Trackbars")
	u_h = cv2.getTrackbarPos("U-H", "Trackbars")
	u_s = cv2.getTrackbarPos("U-S", "Trackbars")
	u_v = cv2.getTrackbarPos("U-V", "Trackbars")

	lower_red = np.array([l_h, l_s, l_v])
	upper_red = np.array([u_h, u_s, u_v])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	kernel = np.ones((5,5), np.uint8)
	mask = cv2.erode(mask, kernel)
	
	#contour detection

	contours, _=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		area= cv2.contourArea(cnt)
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		if area > 400:
			cv2.drawContours(frame, [approx], 0, (0,0,0), 5)

			if len(approx) == 4:
				print("Gate")

	cv2.imshow("Frame", frame)
	cv2.imshow("Mask", mask)

	key=cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()


