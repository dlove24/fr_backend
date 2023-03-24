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

#timer set up
tim=Timer()
timercounter=0
def tick(timer):
    global timercounter
          
while True:
    
    rotl_limit = rotlimit.value()
    if rotl_limit == True:
        print ("rotation limit made")
        sleep(.025)
    vert_limit = vertlimit.value()
    if vert_limit  == True:
        print ("vertical limit made")
        sleep(.025)
    horiz_limit = horizlimit.value()
    if horiz_limit == True:
        print ("horizontal limit made")
        sleep(.025)
        
    grip_limit = griplimit.value()
    if grip_limit == True:
        print ("grip limit made")
        sleep(.025)   
        
    