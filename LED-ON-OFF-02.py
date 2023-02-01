import RPi.GPIO as  GPIO  ## importing GPIO module with alias
GPIO.setmode(GPIO.BCM)   ## Set mode for the entire GPIO mode
#Import time module
import time
# Code
LED_PIN = 17   # Using variable, we are using the pin nr 17
GPIO.setup(LED_PIN, GPIO.IN)    ## GPIO pin nr 17 Input for READ, we can also hardcode the pin nr 17 in the code, better to use the variable
GPIO.setup(LED_PIN, GPIO.OUT)   ## GPIO pin nr 17 output for Write

while True:
    GPIO.setup(LED_PIN, GPIO.HIGH)   ## Power on the LED 
    time.sleep(1)                     # Sleep timer, remember to import the time module import
    GPIO.setup(LED_PIN, GPIO.LOW)   ## Power oFF the LED 
    time.sleep(1)  
# this will cleanup all of the GPIOs to default mode, good to protect the board
GPIO.cleanup()  
 
