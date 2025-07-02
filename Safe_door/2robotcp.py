import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import time

in1 = (6)
in2 = (13)
in3 = (19)
in4 = (26)
en1 = (20)
en2 = (21)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1 = GPIO.PWM(en1,1000)
p1.start(40)
p1.ChangeDutyCycle(0)
p2 = GPIO.PWM(en2,1000)
p2.start(40)
p2.ChangeDutyCycle(0)

def go_forward(speed1, speed2):
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
	p1.ChangeDutyCycle(speed1)
	p2.ChangeDutyCycle(speed2)


def stop():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)

time.sleep(5)
go_forward(60, 60)
time.sleep(5)
stop()
