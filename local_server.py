import socket
import threading
import time

# Standard size used for the header message
header = 64

# Local port and IP Socket settings
port = 5050
ip = "192.168.137.247"#socket.gethostbyname(socket.gethostname())
print("LOCAL SERVER HOSTED ON: ", ip) 
addr = (ip, port)

format = "utf-8"

# Port and IP Socket settings defined for server
Server_port = 5050 # Server's definer port
server_ip = "20.91.176.137"
print("CONNECTING TO: ", server_ip) # Debug
server_addr = (server_ip, Server_port)

# Format for encoding and decoding messages
format = "utf-8"

# Server socket object defined
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr) 

# Client socket object defined
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)

# Server handling new connections and messages
def handle_client(conn, addr):
    print("-" * 5, "New Connection", "-" * 5) # Debug
    connection = True
    while connection is True: # To add connection closed later. 
        # First message is recived and decoded 
        msg_one =conn.recv(header).decode(format)
        if msg_one: # if messages isn't null run the following
            msg_length = int(msg_one) # The main message lenght is defined as int from the decoded message
            msg = conn.recv(msg_length).decode(format) # Main message is recieved with the defined length 
            print("MESSAGE RECIEVED: ", msg) # Debug
            send(msg)
            print("-" * 5, "MESSAGE SENT", "-" * 5)
            
# Main function starts and listens for new devices 
def start():
    server.listen() # Server object listens for new connections
    while True:
        conn, addr = server.accept() # New connection accepted and variables defined
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # New connections varriables, used as arguments for handle function as a thread
        thread.start() # The handle client thread is started so start() can keep listening for new connections

def send(msg):
    # Message encoded 
    message = msg.encode(format)
    # Message length defined from encoded message
    msg_length = len(message)
    # Message length info converted to string and encoded for sending
    length_data = str(msg_length).encode(format)
    # Message length data padded with b strings to header size
    length_data + b' ' * (header - len(length_data))
    # Padded length infermation sent
    client.send(length_data)
    time.sleep(0.05) # Time.sleep to create space between messages 
    # Send the main messages
    client.send(message)
    print("-" * 5, "SENDING MSG TO: ", server_ip, "-" * 5)
    print("SENT MESSAGE: ", msg) # Debug
    print("THE MESSAGE LENGTH IS: ", msg_length) # Debug

start() # Runs the main function
