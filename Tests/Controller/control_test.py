import time
import curses
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit 'q' to quit")
stdscr.refresh()

# set up pin numbering
GPIO.setmode(GPIO.BCM)

# set up pins as output
# motors set 1 (left)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# motors set 2 (right)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

key = ''

while not key == ord('q'):

    key = stdscr.getch()

    stdscr.addch(20, 25, key)
    stdscr.refresh()

    if   key == curses.KEY_UP:
        # move forward
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)

    elif key == curses.KEY_DOWN:
        # move backward
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

    elif key == curses.KEY_RIGHT:
        # turn right
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)

    elif key == curses.KEY_LEFT:
        # turn left
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

    else:
        # break
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)

        GPIO.output(16,  GPIO.HIGH)
        GPIO.output(20,  GPIO.LOW)
        GPIO.output(21, GPIO.LOW)

curses.endwin()
GPIO.cleanup()
