import socket
import threading
import dbConverter
header = 64
port = 5050
ip = socket.gethostbyname(socket.gethostname())
print(ip)
addr = (ip, port)

class Data:
	new_list = []

format = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def handle_client(conn, addr):
	print("NEW CONNECTION")
	connection = True
	while connection is True:
		msg_one = conn.recv(header).decode(format)
		if msg_one:
			msg_length = int(msg_one)
			msg = conn.recv(msg_length).decode(format)
			print(msg)
			print(msg_length)
			Data.new_list = msg.split("/")
			for x in Data.new_list:
				dbConverter.barcode_Split(x)

			

def start():
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		

print("Server starting")
start()
