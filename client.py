import cv2, json, socket, pickle

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
with open("config.json") as file:
    file = json.load(file)
ip = file["ip"]
port = file["port"]
s.bind((ip,port))

while True:
    x=s.recvfrom(1000000)
    data=x[0]
    data=pickle.loads(data)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('Mapkep', data)
    if cv2.waitKey(10) == 13:
        break
