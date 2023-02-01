from imageai.Detection import ObjectDetection
import cv2, socket, pickle, json


def object_detection_on_a_camera():
	detector = ObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath("yolov3.pt")
	detector.loadModel()
	while True:
		camera = cv2.VideoCapture(source)
		ret, frame = camera.read()
		frame = cv2.resize(frame, (640, 360))
		if not ret:
			continue
		detections = detector.detectObjectsFromImage(input_image=frame,
		                                             output_type="array",
		                                             minimum_percentage_probability=30,
		                                             custom_objects=detector.CustomObjects(cell_phone=True)
		                                             )
		for detection in detections[1]:
			obj = json.dumps(detection)
			obj = json.loads(obj)
			cords = obj['box_points']
			cv2.rectangle(frame, (cords[0], cords[1]), (cords[2], cords[3]), (0, 0, 255))
			cv2.putText(frame,
			            obj['name'] + " " + str(obj["percentage_probability"]),
			            (cords[0], cords[1] - 6),
			            cv2.FONT_HERSHEY_DUPLEX,
			            1.0,
			            (0, 0, 0),
			            3)
			cv2.putText(frame,
			            obj['name'] + " " + str(obj["percentage_probability"]),
			            (cords[0], cords[1] - 6),
			            cv2.FONT_HERSHEY_DUPLEX,
			            1.0,
			            (255, 255, 255))
		cv2.imshow("Mapkep", frame)
		ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
		x_as_bytes = pickle.dumps(buffer)
		for i in server_list:
			s.sendto(x_as_bytes, i)
		if cv2.waitKey(10) == 13:
			break
		camera = None


if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)
	server_list = []
	with open("server_list.json") as file:
		file = json.load(file)
		source = file["source"]
	for i in file["server_list"]:
		server_list.append((i["ip"], i["port"]))
	object_detection_on_a_camera()