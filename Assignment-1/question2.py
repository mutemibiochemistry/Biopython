#2converts temparature from degree celcius to degree fahrenheit
degree1 = int(raw_input("Enter degree1: "))		#prompt user to enter value1
degree2 = int(raw_input("Enter degree2: "))		#prompt user to enter value2
print   "C","\t","F"					#print title headers,t character to introduce spaces
if degree1 < degree2:					#determine choice		
	for c in range(degree1,degree2+1):		#set range if choice1 followed
		f = 1.8*c + 32				#formula
		print  int(c),"\t",float(f)		#print output of choice 1
elif degree2 < degree1:					#choice2 incase choice1 is not fulfilled
		for c in range(degree2,degree1+1):	#range of operation
			f = 1.8*c + 32			#formula
			print  int(c),"\t",float(f)	#print output of choice 2



