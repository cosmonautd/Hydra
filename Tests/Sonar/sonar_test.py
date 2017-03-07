import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIG = 37
ECHO = 35

speed_of_sound = 349.10
max_distance = 4.0
max_delta_t = max_distance / speed_of_sound

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

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

print("Distance:", round(distance, 2), "cm")

GPIO.cleanup()
