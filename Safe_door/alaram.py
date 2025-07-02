irsensor_1 = None


import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import time
GPIO.setup((7), GPIO.IN)
GPIO.setup((18), GPIO.OUT)
while True:
  irsensor_1 = GPIO.input(7)
  if irsensor_1 == 1:
    print('Motion detected')
    GPIO.output(18, True)
    time.sleep(2)
    GPIO.output(18, False)
  elif irsensor_1 == 0:
    print('No Motion detected')
    GPIO.output(18, False)
    time.sleep(1)
