from machine import Pin
import time
from time import sleep


#limits
rotlimit= Pin(5, Pin.IN, Pin.PULL_DOWN)
vertlimit= Pin(4, Pin.IN, Pin.PULL_DOWN)
horizlimit= Pin(2, Pin.IN, Pin.PULL_DOWN)
griplimit=Pin(0,Pin.IN, Pin.PULL_DOWN)

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
rotenc= Pin(9, Pin.IN, Pin.PULL_DOWN)
rotenca= Pin(8, Pin.IN, Pin.PULL_DOWN)
vertenc= Pin(7, Pin.IN, Pin.PULL_DOWN)
vertencA= Pin(6, Pin.IN, Pin.PULL_DOWN)
horizenc= Pin(3, Pin.IN, Pin.PULL_UP)
gripenc=Pin(1,Pin.IN, Pin.PULL_DOWN)

#variables
delay=0.05
henc= 0
venc=0
genc=0
renc=0
debounce_time=0
vert_limit = vertlimit.value()
rotl_limit = rotlimit.value()
horiz_limit = horizlimit.value()
grip_limit = griplimit.value()

#encoder varibles
horiz_status=0
vert_status=0
grip_status=0
rot_status=0


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
 
#count functions

def HorizCount(horizenc):
     global henc
     if (horiz_status==0 and (time.ticks_ms()-debounce_time) >2):     
       henc += 1
     else: henc -=1

def VertCount(vertenc):
     global venc
     if (vert_status==0 and (time.ticks_ms()-debounce_time) >2):     
       venc += 1
     else: venc -=1

def GripCount(gripenc):
     global genc
     if (grip_status==0 and (time.ticks_ms()-debounce_time) >2):     
       genc += 1
     else: genc -=1
     
def RotCount(rotenc):
     global renc
     if (rot_status==0 and (time.ticks_ms()-debounce_time) >2):     
       renc += 1
     else: renc -=1     
     
     
#count Irq    
horizenc.irq(trigger=Pin.IRQ_FALLING, handler=HorizCount)
vertenc.irq(trigger=Pin.IRQ_FALLING, handler=VertCount)    
gripenc.irq(trigger=Pin.IRQ_FALLING, handler=GripCount)
rotenc.irq(trigger=Pin.IRQ_FALLING, handler=RotCount)
#moves  
while vert_limit==False or grip_limit == False or horiz_limit == False or rotl_limit == False :
   
    horiz_limit = horizlimit.value()
    if horiz_limit == True:
         horizin.value(0)
      
    else:horizin.value(1)       
                
    vert_limit = vertlimit.value()
    if vert_limit  == True:
        vertup.value(0)
       
    else: vertup.value(1)  
    
    grip_limit = griplimit.value()
    if grip_limit == True:
        opengrip.value(0)
      
    else:opengrip.value(1)
   
    rotl_limit = rotlimit.value()
    if rotl_limit == True:
       rotclk.value(0)
      
    else: rotclk.value(1)

#resets encoders to zero on loop exit
sleep(.1)
henc=0
venc=0
genc=0
renc=0

while True:
                
#prints encoder values in console
        sleep(.2)
        horiz_count= henc
        sleep(delay)
        print("{} arm out pulses".format(horiz_count))      
        
        vert_count= venc
        sleep(delay)
        print("{} vertical pulses".format(vert_count))
    
        grip_count= genc
        sleep(delay)
        print("{} grip pulses".format(grip_count))
        
        rot_count= renc
        sleep(delay)
        print("{} rotation pulses".format(rot_count))




#up down and rotatation via buttons
          
        if downsw.value()==0:
            vertdown.value(1)
            vert_status=0
            sleep(delay)
            print ("down")
        else: vertdown.value(0)
        
        if upsw.value()==0:
            vertup.value(1)
            vert_status=1
            sleep(delay)
            print ("up")
        else: vertup.value(0)
             
#griparm control via buttons
        if armoutsw.value()==0:
            horizout.value(1)
            horiz_status=0
            sleep(delay/2)
            print ("arm out")            
             
        else: horizout.value(0)
         
        if arminsw.value()==0:
            horizin.value(1)
            horiz_status=1        
            sleep(delay)
            print ("arm in")
        else: horizin.value(0) 
          
        if griposw.value()==0:
            opengrip.value(1)
            grip_status=1 
            sleep(delay)
            print ("open")
        else: opengrip.value(0)  
                  
        if gripcsw.value()==0:
            closegrip.value(1)
            grip_status=0
            sleep(delay)
            print ("close")
        else: closegrip.value(0)
        
        if cclksw.value()==0:
            rotcclk.value(1)
            rot_status=0
            sleep(delay)
            print ("anticlock")
        else: rotcclk.value(0)
        
        if clksw.value()==0:
            rotclk.value(1)
            rot_status=1       
            sleep(delay)
            print ("clock")
        else: rotclk.value(0)
                     
                       