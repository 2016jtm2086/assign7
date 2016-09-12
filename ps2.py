
import random
A=0   #initialise number of users
count=0     #initialising no of users in the area of unit distance about MSC
for A in range(1,1001):
	(X,Y)=(random.random()*2- 1, random.random()*2-1)
	A+=1
	
	if((X**2+Y**2)<=1):
		count+=1

perc=(float(count)/1000)*100

print "Percentage of users in unit circle around MSC is %d" %perc
