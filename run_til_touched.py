from ev3dev.ev3 import TouchSensor
import move


ts = TouchSensor('in1')


def main():
	move.straight()
	while 1:
		if ts.value():
			move.halt()
			break


main()
