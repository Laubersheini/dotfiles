import os
import subprocess
import time
import sys   

def roundToNearesFifth(value):
	return value - value % 5

while True:	
	rawValue =  subprocess.getoutput("brightnessctl g")

	rawPercent = (int(rawValue)/255)*100

	sys.stdout.write(str(int(roundToNearesFifth(rawPercent)))+ "\n" )
	sys.stdout.flush()
	time.sleep(1)

