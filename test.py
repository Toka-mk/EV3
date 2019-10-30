from ev3dev.ev3 import ColorSensor
import move


threshold = 50
cs = ColorSensor('in1')


def main():
	move.forward()
	while 1:
		if cs.value() > threshold:
			move.halt()
			break


main()
