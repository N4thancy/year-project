import cv2
import numpy
from pyzbar.pyzbar import decode
from gpiozero import Buzzer

buzzer = Buzzer(20)

def barcode_read():
    cam = cv2.VideoCapture(0)
    cam.set(3,640) # width is 3
    cam.set(4,480) # Height is 4
    while True:
        success, img = cam.read()
        if not decode(img):
            print("No barcode detected")
            pass
        else:
            buzzer.on()
            for barcode in decode(img):
                barcode_data = barcode.data.decode('utf-8')
                print(barcode_data)
        
                cam.release()
                cv2.destroyAllWindows()
                buzzer.off()
                return barcode_data
                #break
                
        
    
        #cv2.imshow('Result',img)
        cv2.waitKey(1)
