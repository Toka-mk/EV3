from ev3dev.ev3 import LargeMotor
from time import sleep

lm = LargeMotor('outA')
rm = LargeMotor('outB')


def halt(stop_action='brake'):  # stop both motors
	lm.stop(stop_action=stop_action)
	rm.stop(stop_action=stop_action)


def stop_after(duration, stop_action='brake'):  # stop both motors after set duration
	if duration:
		sleep(duration)
		halt(stop_action)


def straight(duration=0, speed=500, stop_action='brake'):
	# move in a straight line at set speed for set duration
	# set speed to negative to move backwards; speed range [1000, -1000]
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=speed)
	stop_after(duration, stop_action)


def left(duration=0, speed=500, ratio=.2, stop_action='brake'):
	# turn left with left motor's speed at set ratio compared to right motor
	# set ratio to -1 to have left motor turn completely opposite to right, which allows turning in place
	lm.run_forever(speed_sp=speed*ratio)
	rm.run_forever(speed_sp=speed)
	stop_after(duration, stop_action)


def right(duration=0, speed=500, ratio=.2, stop_action='brake'):
	# turn right with right motor's speed at set ratio compared to let motor
	# set ratio to -1 to have right motor turn completely opposite to left, which allows turning in place
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=speed*ratio)
	stop_after(duration, stop_action)
