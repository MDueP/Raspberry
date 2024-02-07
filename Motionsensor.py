################################
#Moduler og Classes anvendt
import adafruit_hcsr04
############################
#Variabler og objekter
ultrasonic = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=)

async def distance():
    while True:
        lcd.clear()
        lcd.putstr(f"Distance: {ultrasonic.distance_cm()} CM")
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()