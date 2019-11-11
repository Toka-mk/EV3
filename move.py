from ev3dev.ev3 import LargeMotor, Button
from time import sleep

lm = LargeMotor('outA')
rm = LargeMotor('outB')
btn = Button()
sa = 'brake'


def halt(stop_action=sa):  # stop both motors
	lm.stop(stop_action=stop_action)
	rm.stop(stop_action=stop_action)


def stop_after(duration, stop_action=sa):  # stop both motors after set duration
	if duration:
		sleep(duration)
		halt(stop_action)


def straight(duration=0, speed=500, stop_action=sa):
	# move in a straight line at set speed for set duration
	# set speed to negative to move backwards; speed range [1000, -1000]
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=speed)
	stop_after(duration, stop_action)


def left(duration=0, speed=500, ratio=.2, stop_action=sa):
	# turn left with left motor's speed at set ratio compared to right motor
	# set ratio to -1 to have left motor turn completely opposite to right, which allows turning in place
	lm.run_forever(speed_sp=speed*ratio)
	rm.run_forever(speed_sp=speed)
	stop_after(duration, stop_action)


def right(duration=0, speed=500, ratio=.2, stop_action=sa):
	# turn right with right motor's speed at set ratio compared to let motor
	# set ratio to -1 to have right motor turn completely opposite to left, which allows turning in place
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=speed*ratio)
	stop_after(duration, stop_action)


def turn_by_degree(direction, degree=90, stop_action=sa):
	relative_pos = 1260*degree/360

	if direction.lower() in ['l', 'left', '0']:
		rm.run_to_rel_pos(position_sp=relative_pos, speed_sp=500, stop_action=stop_action)
		lm.run_to_rel_pos(position_sp=-relative_pos, speed_sp=500, stop_action=stop_action)
	elif direction.lower() in ['r', 'right', '1']:
		rm.run_to_rel_pos(position_sp=-relative_pos, speed_sp=500, stop_action=stop_action)
		lm.run_to_rel_pos(position_sp=relative_pos, speed_sp=500, stop_action=stop_action)
