#1converts temparature from degree celcius to degree fahrenheit
def convert_celcius_to_fahrenheit(degree):      			#function
	fahrenheit = 1.8*degree + 32 					#conversion formula
	print float(degree),"Celcius ->",fahrenheit, "Fahrenheit"	#send output

test1=convert_celcius_to_fahrenheit(50.0)				#test example
test2=convert_celcius_to_fahrenheit(10.0)
