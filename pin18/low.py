import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


GPIO.output(18, GPIO.LOW)
if GPIO.input(18):
   print("PIN IS HIGH")
else :
   print("PIN IS LOW")
