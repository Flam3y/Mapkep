from notifypy import Notify
import cv2, json, socket, pickle


notification = Notify(
  default_notification_title="Замечен списывающий",
  default_notification_application_name="Маркер",
  default_notification_icon="hand.ico",
  default_notification_audio="sound.wav",
  default_notification_message="Замечен списывающий!")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
with open("config.json") as file:
    file = json.load(file)
ip = file["ip"]
port = file["port"]
s.bind((ip,port))

while True:
    x = s.recvfrom(1000000)
    r = s.recvfrom(1000000)
    data = x[0]
    data=pickle.loads(data)
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow("Mapkep", frame)
    if int.from_bytes(r[0], "big"):
        notification.send()
    if cv2.waitKey(10) == 13:
        break
