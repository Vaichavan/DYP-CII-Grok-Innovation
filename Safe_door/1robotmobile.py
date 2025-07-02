status = None


import sys, os
HOME        = os.path.expanduser('~')
RPI_HOME    = HOME + '/RPI/'
GROK_HOME   = HOME + '/Desktop/Grok-Downloads/'
sys.path.insert(1, RPI_HOME)
from file_watcher import FileWatcher, device_sensor
from grok_library import check_with_simulator,check_with_simulator2, device, sim_device, pin, GrokLib
import threading
grokLib = GrokLib()

device['applicationIdentifier'] = str(os.path.splitext(os.path.basename(__file__))[0])
device['mobile_messages'] = list()

def simulate(list_of_sensors):
    if list_of_sensors is not None:
        global sim_device
        sim_device = list_of_sensors
def startListener1():
    FileWatcher(simulate, 'simulation.json', RPI_HOME, 'config_file')
thread1 = threading.Thread(target=startListener1, args=())
thread1.daemon=True
thread1.start()


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

while True:
  if 'status' in sim_device:
    status = sim_device['status']
    if status == True:
      go_forward(60, 60)
    else:
      stop()
  else:
    go_forward(60, 60)
    time.sleep(0.2)
