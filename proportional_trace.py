from ev3dev.ev3 import ColorSensor
import time, move


cs = ColorSensor('in1')
cs.mode = 'COL-AMBIENT'
t0 = time.time()

speed = 150  # max, min: 1000, -1000
dt = 500  # refresh speed in milliseconds
stop_action = "coast"


def main():

	kp = 1  # proportional gain
	ki = 0  # integral gain
	kd = 0  # derivative gain

	inte = 0  # integral
	prev_error = 0

	target = cs.value()

	while time.time()-t0 < 15:

		error = target - cs.value()
		inte += (error *= dt)
		deri = (error - prev_error) / dt  # derivative

		h = (kp * error) + (ki * inte) + (Kd * deri)


main()
