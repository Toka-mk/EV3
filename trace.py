from ev3dev.ev3 import ColorSensor
import move
from time import time

threshold = 5
cs = ColorSensor('in1')
cs.mode = 'COL-COLOR'
t0 = time()


def main():
	while time()-t0 < 15:
		if cs.value() > threshold:
			move.left(.1, ratio=-.5)
		else:
			move.right(.1, ratio=-.5)


main()
