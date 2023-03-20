import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
import pickle
import socket
import threading
import win10toast
from client_1_ui import Ui_MainWindow
from client_2_ui import Broadcast_Form
from error_ui import Error_Dialog


def exit():
	ClientMainWindow.hide()
	ClientUI.label.clear()
	s.close()


def notify():
	event.clear()
	while ClientMainWindow.isVisible():
		event.wait()
		toaster.show_toast("Маркер",
						   "Замечен списывающий!",
						   icon_path="hand.ico",
						   duration=5,
						   threaded=True)
		while toaster.notification_active(): time.sleep(0.1)
		event.clear()


def connect_to_server():
	global s
	try:
		adress = MainUI.Ip.text().split(" ")
		ip, port = adress[0], adress[1]
		s = socket.create_connection((ip, int(port)))
	except Exception as ex:
		ErrorMainWindow.show()
		ErrorUI.textBrowser.setText(str(ex))
	else:
		ClientMainWindow.show()
		threading.Thread(target=notify).start()
		threading.Thread(target=recv).start()


def recv():
	while ClientMainWindow.isVisible():
		image_bytes = s.recv(1000000)
		count_bytes = s.recv(1000000)
		try:
			data = pickle.loads(image_bytes)
		except:
			image_bytes, count_bytes = count_bytes, image_bytes
		data = pickle.loads(image_bytes)
		frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
		frame = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
		ClientUI.label.setPixmap(QtGui.QPixmap.fromImage(frame))
		if int.from_bytes(count_bytes, "big"):
			event.set()
		else:
			event.clear()
		if cv2.waitKey(10) == 13:
			break


event = threading.Event()
toaster = win10toast.ToastNotifier()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainUI = Ui_MainWindow()
MainUI.setupUi(MainWindow)
MainWindow.show()
MainUI.Connect.clicked.connect(connect_to_server)

ClientMainWindow = QtWidgets.QMainWindow()
ClientUI = Broadcast_Form()
ClientUI.setupUi(ClientMainWindow)
ClientUI.pushButton.clicked.connect(exit)

ErrorMainWindow = QtWidgets.QDialog()
ErrorUI = Error_Dialog()
ErrorUI.setupUi(ErrorMainWindow)

sys.exit(app.exec_())
