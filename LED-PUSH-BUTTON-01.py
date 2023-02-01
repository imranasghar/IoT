import RPi.GPIO as GPIO
import time

LED_PIN = 17  # Connected LED at GPIO pin nr 17
BUTTON_PIN = 26 # connected push button at GPIO pin nr 26

## Setting up the GPIO 
GPIO.setmode(GPIO.BCM)   
GPIO.setup(LED_PIN,GPIO.OUT)
 ## Input button setup 
GPIO.setup(BUTTON_PIN,GPIO.IN) 

## Infinite loop, exit with ctr + C
while True:   ## Infinite loop 
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
