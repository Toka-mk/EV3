from ev3dev.ev3 import LargeMotor
from time import sleep

lm = LargeMotor('outA')
rm = LargeMotor('outB')


def halt():
	lm.stop()
	rm.stop()


def run_for(duration):
	if duration:
		sleep(duration)
		halt()


def forward(duration=0, speed=500):
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=speed)
	run_for(duration)


def left(duration=0, speed=500, ratio=3):
	lm.run_forever(speed_sp=(speed/ratio) if ratio else 0)
	rm.run_forever(speed_sp=speed)
	run_for(duration)


def right(duration=0, speed=500, ratio=3):
	lm.run_forever(speed_sp=speed)
	rm.run_forever(speed_sp=(speed/ratio) if ratio else 0)
	run_for(duration)
