from ev3dev.ev3 import InfraredSensor, TouchSensor
import move
from time import time, sleep
import numpy as np


threshold = 10
ir = InfraredSensor('in4')
ts = TouchSensor('in1')
t0 = time()


def main():

	# while time()-t0 < 30 and not ts.value():
	while 1:
		if ir.value() > threshold:
			# move.straight(.5, -500, 'brake')
			move.turn_by_degree('r', 90, stop_action='brake')
			sleep(2)
		else:
			move.straight(.1, stop_action='coast')
		if ts.value() == 1:
			break
	exit()


main()
