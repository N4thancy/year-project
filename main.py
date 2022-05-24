from gpiozero import Button
import time
import capture
import led_control
import client

button = Button(16)

def interrupt():
    print("button pressed")
    led_control.set_yellow()
    client.send(capture.barcode_read())

button.when_pressed = interrupt

while True:
    time.sleep(0.5)
