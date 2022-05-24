import socket
import threading

# Standard size used for the header message
header = 64
# Local port and IP Socket settings
port = 5050 # Pick a port
ip = socket.gethostbyname(socket.gethostname())
print(ip) #Printing the host IP for use on client
addr = (ip, port)

# Format for encoding and decoding messages
format = "utf-8"

# Server socket object defined
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr) # Socket bound to local address

# Server handling new connections and messages
def handle_client(conn, addr):
    print("New Connection") # Debug
    connection = True
    while connection is True: # To add connection closed later. 
        # First message is recived and decoded 
        msg_one =conn.recv(header).decode.format()
        if msg_one: # if messages isn't null run the following
            msg_length = int(msg_one) # The main message lenght is defined as int from the decoded message
            msg = conn.recv(msg_length).decode(format) # Main message is recieved with the defined length 
            print(msg) # Debug
            print(msg_length) # Debug

# Main function starts and listens for new devices 
def start():
    server.listen() # Server object listens for new connections
    while True:
        conn, addr = server.accept() # New connection accepted and variables defined
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # New connections varriables, used as arguments for handle function as a thread
        thread.start() # The handle client thread is started so start() can keep listening for new connections
        

print("Server is starting") # debug
start() # Runs the main function
