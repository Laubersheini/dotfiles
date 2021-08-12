import os
import subprocess
import time
import sys
 
#this script periodically checks if a bluetooth device(my headset) is connected or not and outputs aproproate fontawesome characters 
while True:
	rawValue =  subprocess.getoutput("pactl get-default-sink")
	if "bluez" in rawValue:
		sys.stdout.write("\n")
	else:
		sys.stdout.write("\n")

	sys.stdout.flush()
	time.sleep(2)

                                                                                                                                                  
                              


