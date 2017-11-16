import RPi.GPIO as GPIO
import sys, getopt


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)

if GPIO.input(int(sys.argv[1])):
   print(sys.argv[1]+" PIN IS HIGH")
else :
   print(sys.argv[1]+" PIN IS LOW")
