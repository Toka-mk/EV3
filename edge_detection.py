from ev3dev.ev3 import InfraredSensor, TouchSensor
import move
from time import time

threshold = 10
ir = InfraredSensor('in4')
ts = TouchSensor('in2')
t0 = time()


def right90():
	move.right(2, 500, -1, 'coast')


def main():
	while time()-t0 < 50 and not ts.value():

		if ir.value() > threshold:
			move.straight(.5, stop_action='coast')
		else:


	exit()


# main()
