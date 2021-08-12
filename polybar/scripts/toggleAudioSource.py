import os
import subprocess
import time
import sys
  
#this script toggles the current audiosource 
rawSources  =  subprocess.getoutput("pactl list short sinks")
currentSink =   subprocess.getoutput("pactl get-default-sink") 

sinks = rawSources.split("\n")
sinkIds = []
for sink in sinks:
	sinkIds.append(sink[0:1])

currentSinkIndex = -1
for i in range(len(sinks)):
	if currentSink in sinks[i]:
		currentSinkIndex = i

print(currentSinkIndex)
if currentSinkIndex +1   < len(sinks):
	print("pactl set-default-sink " + sinkIds[currentSinkIndex +1])
	os.system("pactl set-default-sink " + sinkIds[currentSinkIndex +1])
else:
	os.system("pactl set-default-sink "+sinkIds[0])
