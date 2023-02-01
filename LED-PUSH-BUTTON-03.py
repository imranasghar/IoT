## See circuit
## imporvment in the code of LED-PUSH-BUTTON-02.py
## Code optimization using list, functions, loops
## Import and GPIO setup 
import RPi.GPIO as GPIO
import time  ## import time library 

## use arrays,linklist instead variables 
LED_PIN_LIST = [17, 27, 22]

## button variable 
BUTTON_PIN = 26

# Function definition to power on the LEDs 
def power_on_selected_led_only(selected_led_pin):
    if selected_led_pin not in LED_PIN_LIST:   ## to avoid the any additional pin in the array-list
        return                                     # return from function with nothing, like exit
    for pin in LED_PIN_LIST:
        if pin == selected_led_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)     # here End of function 
            
## GPIO initilization
GPIO.setmode(GPIO.BCM)   ## Setting up the GPIO initilization

for pin in LED_PIN_LIST:
    GPIO.setup(pin,GPIO.OUT)     # pin is a local variable accessing the array elments
GPIO.setup(BUTTON_PIN,GPIO.IN)  ## Input button setup 

## Poweroff the LED, just incase, state initilization 
for pin LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0

while True:   ## Infinite loop 
    time.sleep(0.01)  ## timesleep for saving CPU 
    button_state = GPIO.input(BUTTON_PIN)
    if butto_state !=previous_button_state:
        previous_button_state = button_state ## when state is different 
        if button_state == GPIO.HIGH:
            #use a function to power on LEDS
            power_on_selected_led_only(LED_PIN[]led_index])   # element indexing
            led_index += 1
            if led_index > len(LED_PIN_LIST):   # lengh function return back the lengh of the list
                led_index = 0
GPIO.cleanup()  ## GPIO cleanup
