from machine import Pin
from time import sleep

opengrip= Pin(10, Pin.OUT)
closegrip= Pin(11, Pin.OUT)
horizout= Pin(12, Pin.OUT)
horizin= Pin(13, Pin.OUT)
vertdown= Pin(14, Pin.OUT)
vertup=Pin(15, Pin.OUT)
rotclk=Pin(16, Pin.OUT)
rotcclk= Pin(17, Pin.OUT)
led = machine.Pin("LED", machine.Pin.OUT)

    
while True:
    led.toggle()
    sleep(0.25)
    opengrip.toggle()
    sleep(0.25)
    closegrip.toggle()
    sleep(0.25)
    horizout.toggle()
    sleep(0.25)
    horizin.toggle()
    sleep(0.25)
    vertdown.toggle()
    sleep(0.25)
    vertup.toggle()
    sleep(0.25)
    rotclk.toggle()
    sleep(0.5)
    rotcclk.toggle()
    sleep(0.25)
    
       
        
        
       
        
         
 