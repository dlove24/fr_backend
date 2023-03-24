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

#switches
upsw=Pin(18,Pin.IN, Pin.PULL_UP)
downsw=Pin(19,Pin.IN, Pin.PULL_UP)
  
def openabit():  
    vertdown.value(1)
    sleep(1.0)
    vertdown.value(0)
    
    horizout.value(1)
    sleep(1.0)
    horizout.value(0)
    
    rotcclk.value(1)
    sleep(1.0)
    rotcclk.value(0)
    
    closegrip.value(1)
    sleep(0.6)
    closegrip.value(0)
    
def down():
    vertdown.value(1)
    sleep(0.5)
   
def home():

    rotl_limit = rotlimit.value()
    if rotl_limit == True:
       rotclk.value(0)
       print("rotation limit made")
    else: rotclk.value(1)
     
      
    vert_limit = vertlimit.value()
    if vert_limit  == True:
        vertup.value(0)
        print("vertical limit made")
    else: vertup.value(1)
    
            
    horiz_limit = horizlimit.value()
    if horiz_limit == True:
         horizin.value(0)
         print("horizontal limit made")
    else: horizin.value(1) 
   

    grip_limit = griplimit.value()
    if grip_limit == True:
        opengrip.value(0)
        print("grip limit made")
    else: opengrip.value(1)         



while True:       
        if 	downsw.value()==0:
            vertdown.value(1)
            sleep(0.5)
            print ("down")
        else: vertdown.value(1)
        
        
            
            