import time
import RPi.GPIO as GPIO

# set up pin numbering
GPIO.setmode(GPIO.BCM)

# set up pins as output
# motors set 1 (left)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# motors set 2 (right)
GPIO.setup(5,  GPIO.OUT)
GPIO.setup(6,  GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

command = ""

while not command == "quit":
    command = raw_input("Command $ ")
    
    if " " in command:
        [direction, steps] = command.split(" ")
        steps = float(steps)
    else:
        direction = command
        steps = 1
    
    print direction, steps

    if   direction == "up":
        # move forward
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)

        GPIO.output(5,  GPIO.HIGH)
        GPIO.output(6,  GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)

        time.sleep(steps*1.5)

    elif direction == "down":
        # move backward
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)

        GPIO.output(5,  GPIO.HIGH)
        GPIO.output(6,  GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)

        time.sleep(steps*1.5)

    elif direction == "left":
        # turn left
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        
        GPIO.output(5,  GPIO.HIGH)
        GPIO.output(6,  GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        
        time.sleep(steps*1.25)
        
    elif direction == "right":
        # turn right
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
        
        GPIO.output(5,  GPIO.HIGH)
        GPIO.output(6,  GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        
        time.sleep(steps*1.25)

    # break
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

    GPIO.output(5,  GPIO.HIGH)
    GPIO.output(6,  GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

    time.sleep(0.5)

GPIO.cleanup()
