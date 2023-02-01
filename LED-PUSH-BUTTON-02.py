## Tested and working system, see circuit
## Import and GPIO setup 
import RPi.GPIO as GPIO
import time  ## import time library 

#variables 

LED_1_PIN = 17
LED_2_PIN = 27
LED_3_PIN = 22
## button variable 
BUTTON_PIN = 26

## GPIO initilization
GPIO.setmode(GPIO.BCM)   ## Setting up the GPIO initilization
GPIO.setup(LED_1_PIN,GPIO.OUT)  ## Inut LED-1 setup 
GPIO.setup(LED_2_PIN,GPIO.OUT)  ## Inut LED-2 setup 
GPIO.setup(LED_3_PIN,GPIO.OUT)   ## Inut LED-3 setup 
GPIO.setup(BUTTON_PIN,GPIO.IN)  ## Inut button setup 

## Poweroff the LED, just incase, state initilization 
GPIO.output(LED_1_PIN, GPIO.LOW)
GPIO.output(LED_2_PIN, GPIO.LOW)
GPIO.output(LED_3_PIN, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0
while True:   ## Infinite loop 
    time.sleep(1)  ## timesleep for saving CPU 
    button_state = GPIO.input(BUTTON_PIN)
    if butto_state !=previous_button_state:
        previous_button_state = button_state ## when state is different 
        if button_state == GPIO.HIGH:
           if led_index == 0:
            # power on LED 1
            GPIO.output(LED_1_PIN, GPIO.HIGH)
            GPIO.output(LED_2_PIN, GPIO.LOW)
            GPIO.output(LED_3_PIN, GPIO.LOW)
            led_index = 1
           elif led_index == 1
            # power on LED 2
            GPIO.output(LED_1_PIN, GPIO.LOW)
            GPIO.output(LED_2_PIN, GPIO.HIGH)
            GPIO.output(LED_3_PIN, GPIO.LOW)
            led_index = 2
           else:
            # power on LED 3
            GPIO.output(LED_1_PIN, GPIO.LOW)
            GPIO.output(LED_2_PIN, GPIO.LOW)
            GPIO.output(LED_3_PIN, GPIO.HIGH)
            led_index = 0
           
## GPIO cleanup 
GPIO.cleanup()  
