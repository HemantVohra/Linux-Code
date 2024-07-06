from gpiozero import LED
from signal import pause
from time import sleep

led1 = LED(13)
led2 = LED(19)
led3 = LED(26)

try:
    while True:
        # Forward sequence
        led1.on()
        sleep(0.5)
        led1.off()
        
        sleep(0.5)
        
        led2.on()
        sleep(0.5)
        led2.off()
        
        sleep(0.5)
        
        led3.on()
        sleep(0.5)
        led3.off()
        
        sleep(0.5)
        
        # Reverse sequence
        led2.on()
        sleep(0.5)
        led2.off()
        
        sleep(0.5)
        
        led1.on()
        sleep(0.5)
        led1.off()
        
        sleep(0.5)
        
except KeyboardInterrupt:
    pass
