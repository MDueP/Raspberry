#from gpiozero import LED
#from time import sleep

#led = LED(17)

#while True:
#    led.on()
#    sleep(1)
#    led.off()
#    sleep(1)

from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0
    sleep(1)
    led.value = 0.5
    sleep(1)
    led.value = 1
    sleep(1)