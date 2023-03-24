from machine import Pin
import time
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

#encoders
rotencB= Pin(9, Pin.IN, Pin.PULL_DOWN)
rotencA= Pin(8, Pin.IN, Pin.PULL_DOWN)
vertencB= Pin(7, Pin.IN, Pin.PULL_DOWN)
vertencA= Pin(6, Pin.IN, Pin.PULL_DOWN)
horizenc= Pin(3, Pin.IN, Pin.PULL_UP)
gripenc=Pin(1,Pin.IN, Pin.PULL_DOWN)

#count functions

def HorizCount(horizenc):
     global henc
     if (horiz_status==0 and (time.ticks_ms()-debounce_time) >300):     
       henc += 1
     else: henc -=1
    
#count Irq    
horizenc.irq(trigger=Pin.IRQ_FALLING, handler=HorizCount)

#limits
rotlimit= Pin(5, Pin.IN, Pin.PULL_DOWN)
vertlimit= Pin(4, Pin.IN, Pin.PULL_DOWN)
horizlimit= Pin(2, Pin.IN, Pin.PULL_DOWN)
griplimit=Pin(0,Pin.IN, Pin.PULL_DOWN)

#switches
upsw=Pin(18,Pin.IN, Pin.PULL_UP)
downsw=Pin(19,Pin.IN, Pin.PULL_UP)
cclksw=Pin(20,Pin.IN, Pin.PULL_UP)
clksw=Pin(21,Pin.IN, Pin.PULL_UP)
armoutsw=Pin(26,Pin.IN, Pin.PULL_UP)
arminsw=Pin(27,Pin.IN, Pin.PULL_UP)
griposw=Pin(28,Pin.IN, Pin.PULL_UP)
gripcsw=Pin(22,Pin.IN, Pin.PULL_UP)

#variables
delay=0.15
henc= 0
debounce_time=0
vert_limit = vertlimit.value()
rotl_limit = rotlimit.value()
horiz_limit = horizlimit.value()
grip_limit = griplimit.value()

#moves  

def off():
    opengrip.value(0)
    closegrip.value(0)
    horizout.value(0)
    horizin.value(0)
    vertdown.value(0)
    vertup.value(0)
    rotclk.value(0)
    rotcclk.value(0)
 
def down():           
     vertdown.value(1)
     sleep(delay)
     print ("down")
     
def up():
    vertup.value(1)
    sleep(delay)
    print ("up")

def anticlk():
    rotcclk.value(1)
    sleep(delay)
    print ("anticlock")
def clk():
    rotclk.value(1)
    sleep(delay)
    print ("clock")#
def armout():
    horizout.value(1)
    horiz_status=0
    sleep(delay)
    print("arm out")

def armin():
    horizin.value(1)
    horiz_status=1        
    sleep(delay)
    print ("arm in")
    
def gripopen():
    opengrip.value(1)
    sleep(delay)
    print ("open")

def close_grip():
    closegrip.value(1)
    sleep(delay)
    print ("close") 

#startup conditions and routine


#home routine
    
while vert_limit==False or grip_limit == False or horiz_limit == False or rotl_limit == False :
   
    horiz_limit = horizlimit.value()
    if horiz_limit == True:
         horizin.value(0)
         print("horizontal limit made")
    else:horizin.value(1)
       
                
    vert_limit = vertlimit.value()
    if vert_limit  == True:
        vertup.value(0)
        print("vertical limit made")
    else: vertup.value(1)
   
    
    grip_limit = griplimit.value()
    if grip_limit == True:
        opengrip.value(0)
        print("grip limit made")
    else:opengrip.value(1)
   
    rotl_limit = rotlimit.value()
    if rotl_limit == True:
       rotclk.value(0)
       print("rotation limit made")
    else: rotclk.value(1)
          
while True:
        counted= henc
        sleep(delay)
        print("{} arm out pulses".format(counted))
     
#up down and rotatation  
            
        if downsw.value()==0:
            down()
        else: vertdown.value(0)
        
        if upsw.value()==0:
           up() 
        else: vertup.value(0)
        
        if cclksw.value()==0:
            anticlk()
        else: rotcclk.value(0)
        
        if clksw.value()==0:
            clk()
        else: rotclk.value(0)       
#griparm
        if armoutsw.value()==0:
            armout()
        else: horizout.value(0)
         
        if arminsw.value()==0:
            armin()
            
        else: horizin.value(0) 
          
        if griposw.value()==0:
            gripopen()
        else: opengrip.value(0)  
                  
        if gripcsw.value()==0:
            close_grip()
        else: closegrip.value(0) 
            
    
        
        
            
            