import socket
import threading
import dbConverter
import subprocess
import time

# Standard size used for the header message
header = 64

# Local port and IP Socket settings
port = 5050
ip = socket.gethostbyname(socket.gethostname())
print(ip) #Debug
addr = (ip, port)

# Class for holding the list of barcodes 
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
			print("NEW MESSAGE")
			msg_length = int(msg_one)
			msg = conn.recv(msg_length).decode(format)
			print(msg) # Debug
			print(msg_length)# Debug

			# Splits the received data by every / and places the split segments in a list
			Data.new_list = msg.split("/")
			print("RECIEVES CHECKOUTS:", len(Data.new_list))
			print(Data.new_list)
			# Goes through the list and runs it through dbConverter. 
			for x in Data.new_list:
				print("-" * 5, "NEW INPUT", "-" * 5)
				print("Updating database with:", x)
				dbConverter.barcode_Split(x)
				print("-" * 15)
				time.sleep(0.05)

			
# Main function starts and listens for new devices
def start():
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()

print("SERVER STARTING")
# creates a thread for running the main start function of the database handling, so a subprocess can be started to run the website
main_thread = threading.Thread(target = start)
# Start function which listens and handles new clients
main_thread.start()
# Runs the website as a subprocess 
subprocess.run(['python3', '/home/azureuser/Documents/app.py'])
