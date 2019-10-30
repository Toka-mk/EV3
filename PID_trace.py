# WIP

from ev3dev.ev3 import ColorSensor
import time
import move


cs = ColorSensor('in1')
cs.mode = 'COL-REFLECT'
t0 = time.time()

speed = 150
dt = 500
stop_action = "coast"


def main():

	kp = 1  # proportional gain
	ki = 0  # integral gain
	kd = 0  # derivative gain

	integral = 0
	prev_error = 0

	target = cs.value()

	while time.time()-t0 < 15:

		error = target - cs.value()
		# noinspection PyRedundantParentheses,SyntaxError
		integral += (error *= dt)
		derivative = (error - prev_error) / dt

		h = (kp * error) + (ki * integral) + (kd * derivative)


main()
