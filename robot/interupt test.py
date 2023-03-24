from machine import Pin

interrupt_flag=0
count=0
debounce_time=0


pin = Pin(18,Pin.IN,Pin.PULL_UP)

def callback(pin):
    global interrupt_flag
    interrupt_flag=1
    counter+=1
    print("Button Pressed")
    print("Count={}".format(counter)

pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)
          
while True:
    if interrupt_flag is 1:
        print("Interrupt has occured")
        interrupt_flag=0
        