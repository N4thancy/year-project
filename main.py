from gpiozero import Button
import time
import capture as capture
# import led_control
import client
import socket
import time

class Checkout:
    shop_list = ""


# Standard size used for the header message
header = 64
# Port and IP Socket settings defined for server
port = 5050 # Server's definer port

server_ip = "192.168.137.247" #LOCAL SERVER IP
print(server_ip) # Debug
addr = (server_ip, port)

# Format for encoding and decoding messages
format = "utf-8"

# Button object defined
button = Button(16)

# Client socket object defined and connected to server address
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)


# Send function sends a message to the server
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
    print("[SENDING MSG] to", server_ip)
    print(msg) # Debug
    print(msg_length) # Debug


def scan():
    print("BUTTON PRESSED")
    # led_control.set_yellow()
    if Checkout.shop_list == "":
        Checkout.shop_list = capture.barcode_read()
    else:
        Checkout.shop_list = (Checkout.shop_list + "/" + capture.barcode_read())
    print(Checkout.shop_list)

def send_all():
    send(Checkout.shop_list)
    print("SENDING SUCCESSFUL")
    Checkout.shop_list = ""



button.when_pressed = scan
button.when_held = send_all

print("PROGRAM STARTET")
while True: 
    time.sleep(0.5)
