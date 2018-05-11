#Prompt for Transmission rate and power
x = int(input("What is the desired transmission rate(in ms, has to be between 30 ms and 10320 ms)? "))
global txPower
while (x < 30)|(x > 10320): 
	x = int(input("The number is outside the range. What is the desired transmission rate(in ms, has to be between 30 ms and 10320 ms)? "))

y=int(input("What is the desired transmission power? Must be between +0 and 15. "))
var = 1
while var == 1:
	if (y >= 0 and y <= 15):
		break
	y=int(input("The number is outside the range. What is the desired transmission power? Must be between 0 and 15. "))



print("\n \n The selected transmission rate is %s ms " % x)
print(" The selected transmission power is %s (value from 0 to 15) " % y)

# X is now the Transmission rate. Y is the transmission power. Major and Minor are set to 0001

txPower=y
import os
os.system("./bled112_ibeacon.py -s -i %s -j 0001 -n 0001" % x)

