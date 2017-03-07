import RPi.GPIO as GPIO
import signal
import time
import sys

GPIO.setmode(GPIO.BOARD)

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

TRIG = 37
ECHO = 35

sampling_rate = 20.0
speed_of_sound = 349.10
max_distance = 4.0
max_delta_t = max_distance / speed_of_sound

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

print ("Sampling Rate:", sampling_rate, "Hz")
print ("Distances (cm)")

while True:

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
      start_t = time.time()

    while GPIO.input(ECHO) == 1 and time.time() - start_t < max_delta_t:
      end_t = time.time()

    if end_t - start_t < max_delta_t:
        delta_t = end_t - start_t
        distance = 100*(0.5 * delta_t * speed_of_sound)
    else:
        distance = -1

    print (round(distance, 2))

    time.sleep(1/sampling_rate)
