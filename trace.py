from ev3dev.ev3 import ColorSensor
import move
import time

threshold = 5
cs = ColorSensor('in1')
cs.mode = 'COL-COLOR'
t0 = time.time()


def main():
	while time.time()-t0 < 15:
		if cs.value() > threshold:
			move.left(.1, ratio=-2)
		else:
			move.right(.1, ratio=-2)


main()
