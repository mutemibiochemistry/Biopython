#Write a program that asks the user for a space separated list of data points (i.e. floating point numbers), then uses appropriate functions from previous questions to calculate and output the standard deviation of those numbers.
nos = ( [1,2,3,4,5,6] )
def mean_mylist(nos):
	if len(nos) == 0:
		return
	else:
		total = sum(nos)
		ave = 1.0*total/len(nos)
		return ave
ave = mean_mylist (nos)
def variation(nos):
	a=0
	mean_mylist(nos)
	
	for i in nos:
		a= a + (i - ave)**2
		variance=a/len(nos)-1
	return variance
var = variation (nos)
from math import sqrt
standardvariation= sqrt(var)
print standardvariation
