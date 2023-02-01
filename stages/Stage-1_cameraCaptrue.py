import cv2

source = 0
camera = cv2.VideoCapture(source)

while True:
	ret, frame = camera.read()
	if not ret:
		continue
	cv2.imshow("Mapkep", frame)
	if cv2.waitKey(10) == 13:
		break
