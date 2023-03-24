from machine import Pin
from machine import Pin, Timer
from time import sleep
#outputs
opengrip= Pin(10, Pin.OUT)
closegrip= Pin(11, Pin.OUT)
horizout= Pin(12, Pin.OUT)
horizin= Pin(13, Pin.OUT)
vertdown= Pin(14, Pin.OUT)
vertup=Pin(15, Pin.OUT)
rotclk=Pin(16, Pin.OUT)
rotcclk= Pin(17, Pin.OUT)
led = machine.Pin("LED", machine.Pin.OUT)
#inputs
rotencoderB= Pin(9, Pin.IN, Pin.PULL_DOWN)
rotencoderA= Pin(8, Pin.IN, Pin.PULL_DOWN)
vertencoderB= Pin(7, Pin.IN, Pin.PULL_DOWN)
vertencoderA= Pin(6, Pin.IN, Pin.PULL_DOWN)
rotlimit= Pin(5, Pin.IN, Pin.PULL_DOWN)
vertlimit= Pin(4, Pin.IN, Pin.PULL_DOWN)
horizencoderB= Pin(3, Pin.IN, Pin.PULL_DOWN)
horizlimit= Pin(2, Pin.IN, Pin.PULL_DOWN)
gripencoder=Pin(1,Pin.IN, Pin.PULL_DOWN)
griplimit=Pin(0,Pin.IN, Pin.PULL_DOWN)

while True:
    vertdown.value(1)
    sleep(1.0)
    vertdown.value(0)
    
    horizout.value(1)
    sleep(1.0)
    horizout.value(0)
    
    rotcclk.value(1)
    sleep(1.5)
    rotcclk.value(0)
    
    closegrip.value(1)
    sleep(1.2)
    closegrip.value(0)
    
    
    break																																

          

  
    
    