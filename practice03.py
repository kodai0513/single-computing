from gpiozero import LED
from time import sleep

led24 = LED(24)
led25 = LED(25)

try:
    while True:
        led24.on()
        led25.off()
        sleep(1)
        led24.off()
        led25.on()
        sleep(1)
    
except KeyboardInterrupt:
    pass

led24.close()
led25.close()