import socket
import time

# Standard size used for the header message
header = 64
# Port and IP Socket settings defined for server
port = 5050 # Server's definer port
server_ip = "192.168.137.247"
print(server_ip) # Debug
addr = (server_ip, port)

# Format for encoding and decoding messages
format = "utf-8"

# Client socket object defined and connected to server address
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# Main function sends a message to the server
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
    print(msg) # Debug
    print(msg_length) # Debug



test_list = ["Besked 1", "Besked 2", "Besked 3","Besked 4"]

# Run the main send function to send the message "Hej" to the server
#send("Hej") 
"""
for x in test_list:
    time.sleep(0.5)
    send(x)

"""
