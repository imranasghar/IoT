## sudo apt-get install python-rpi.gpio python3-rpi.gpio 
## importing GPIO module with alias
import RPi.GPIO as  GPIO  
import time

GPIO.setwarnings(False)
 ## Set mode for the entire GPIO mode
GPIO.setmode(GPIO.BCM)  
GPIO.setup(17,GPIO.OUT)

# Using variable, we are using the pin nr 17
LED_PIN = 17  

print("Turning on the LED")
GPIO.output(17, GPIO.HIGH)   ## Power on the LED 
time.sleep(1)
print("Turning off the LED")                     # Sleep timer, remember to import the time module import
GPIO.output(17, GPIO.LOW)   ## Power oFF the LED 

### Toggle multiple times 
time.sleep(1) 
print("Turning on the LED")
GPIO.output(17, GPIO.HIGH)
time.sleep(1)
print("Turning off the LED")                     # Sleep timer, remember to import the time module import
GPIO.output(17, GPIO.LOW)

print("Cleaup and closing the programe")
GPIO.cleanup()   ## this will cleanup all of the GPIOs to default mode, good to protect the board
