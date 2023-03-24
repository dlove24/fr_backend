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
rotencoderB= Pin(9, Pin.IN, PULL_DOWN)
rotencoderA= Pin(8, Pin.IN, PULL_DOWN)
vertencoderB= Pin(7, Pin.IN, PULL_DOWN)
vertencoderA= Pin(6, Pin.IN, PULL_DOWN)
rotlimit= Pin(5, Pin.In, PULL_DOWN)
vertlimit= Pin(4, Pin.In, PULL_DOWN)
horizencoderB Pin(3, Pin.IN, PULL_DOWN)
horizimit= Pin(2, Pin.In, PULL_DOWN)
gripencoder=Pin(1,Pin.IN, PULL_DOWN)
griplimit=Pin(0,Pin.IN, PULL_DOWN)

#timer set up
tim=Timer()
timercounter=0
def tick(timer)
    globaltimercounter
    
    


    
while True:
    logic_state = rotlimit.value()
    if logic_state == True:
        print ("rotation limit made")
    else
        print()
    
    #led.toggle()
    #sleep(0.25)
    #opengrip.toggle()
    #sleep(0.25)
    #closegrip.toggle()
    #sleep(0.25)
    #horizout.toggle()
    #sleep(0.25)
   # horizin.toggle()
    #sleep(0.25)
    #vertdown.toggle()
    #sleep(0.25)
    #vertup.toggle()
    #sleep(0.25)
    #rotclk.toggle()
    #sleep(0.5)
    #rotcclk.toggle()
    #sleep(0.25)
    
       
        
        
       
        
         
 