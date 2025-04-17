from gpiozero import LED
from time import sleep

led24 = LED(24)
led25 = LED(25)

flashing_time = 3
try:
    while flashing_time > 0:
        led24.on()
        led25.off()
        sleep(flashing_time)
        led24.off()
        led25.on()
        sleep(flashing_time)
        flashing_time -= 0.1
    
except KeyboardInterrupt:
    pass

led24.close()
led25.close()
