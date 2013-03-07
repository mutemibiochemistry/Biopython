#enter floats
nos = raw_input("Enter nos: ")
counter = 0
total = 0

while nos != '':
	counter = counter + 1
	total = total + float(nos)
	nos = raw_input("Enter nos: ")
	if nos == '':
		command= raw_input("Enter command: ")
		if command == 'mean':
			print 'mean is:', total/counter
		if command == 'sum':			
			print 'sum is:', total
		else:
			if command == 'quit':
				quit
			
			
		
			


