from ultralytics import YOLO
import cv2
import numpy as np
import socket
import json
import pickle
import threading


def on_connection(clientsocket, addr):
	while True:
		clientsocket.send(send_data)
		clientsocket.send(detections)
		previous = send_data
		while previous == send_data:
			pass
	clientsocket.close()


def accept_connections():
	while True:
		c, addr = s.accept()
		threading.Thread(target=on_connection, args=(c, addr)).start()


with open("server_config.json") as file:
	file = json.load(file)
	source = file["source"]
	ip, port = file["ip"], file["port"]

s = socket.socket(socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)
s.bind((ip, port))
s.listen(5)

with open("server_config.json") as file:
	file = json.load(file)
	source = file["source"]

model = YOLO("yolov8n.onnx", task="detect")
camera = cv2.VideoCapture(source)

ret, image = camera.read()

ret, buffer = cv2.imencode(".jpg", cv2.resize(image, (480, 640)), [int(cv2.IMWRITE_JPEG_QUALITY), 30])
send_data, detections = pickle.dumps(buffer), (0).to_bytes(1, byteorder="big")

threading.Thread(target=accept_connections).start()
event = threading.Event()

camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
	ret, image = camera.read()

	result = model.predict(image, imgsz=640)

	coordinates = result[0].boxes.numpy().boxes

	if len(coordinates) != 0:
		for param in coordinates:
			cv2.rectangle(image, (int(param[0]), int(param[1])), (int(param[2]), int(param[3])), (0, 0, 255))
			cv2.putText(image,
						"phone" + " " + str(round(param[4], 2)),
						(int(param[0]), int(param[1] - 6)),
						cv2.FONT_HERSHEY_DUPLEX,
						1.0,
						(0, 0, 0),
						3)
			cv2.putText(image,
						"phone" + " " + str(round(param[4], 2)),
						(int(param[0]), int(param[1] - 6)),
						cv2.FONT_HERSHEY_DUPLEX,
						1.0,
						(255, 255, 255),
						1)
	ret, buffer = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
	send_data, detections = pickle.dumps(buffer), int(len(coordinates) != 0).to_bytes(1, byteorder="big")
	cv2.imshow("Mapkep", image)
	if cv2.waitKey(10) == 13:
		break


s.close()
