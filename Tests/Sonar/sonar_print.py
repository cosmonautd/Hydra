import RPi.GPIO as GPIO
import signal
import time
import sys
GPIO.setmode(GPIO.BCM)

def sigint_handler(signum, instant):
    """
    Capture SIGINT signal and quit safely.
    """
    clean()
    sys.exit()

# Activate capture of SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, sigint_handler)

def clean():
    GPIO.cleanup()

TRIG = 26
ECHO = 19

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
time.sleep(2)

frq = 20.0

print ("Frequency:", frq, "Hz")
print ("Distances (cm)")

while True:

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1 or time.time() - pulse_start > 1:
      pulse_end = time.time()

    if pulse_end - pulse_start < 1:
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
    else:
        distance = -1

    print (distance)

    time.sleep(1/frq)
