import socket
import threading
import dbConverter
import subprocess
from pathlib import Path

# Standard size used for the header message
header = 64

# Local port and IP Socket settings
port = 5050
ip = socket.gethostbyname(socket.gethostname())
print(ip) #Debug
addr = (ip, port)

class Data:
	new_list = []

# Format for encoding and decoding messages
format = "utf-8"

# Server socket object defined
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

# Server handling new connections and messages
def handle_client(conn, addr):
	print("NEW CONNECTION") # Debug
	connection = True
	while connection is True: # To possibly add a connection closed later.
		msg_one = conn.recv(header).decode(format)
		if msg_one:  # if message received isn't null run the following
			msg_length = int(msg_one)
			msg = conn.recv(msg_length).decode(format)
			print(msg) # Debug
			print(msg_length)# Debug

			# Splits the received data by every / and places the split segments in a list
			Data.new_list = msg.split("/")
			# Goes through the list and runs it through dbConverter. 
			for x in Data.new_list:
				dbConverter.barcode_Split(x)

			
# Main function starts and listens for new devices
def start():
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()

print("Server starting")

# Runs the website as a subprocess 
subprocess.run(['python3', '/home/azureuser/Documents/app.py'])

# Start function which listens and handles new clients
start()
