#enters sequence of nos ending with a blank line then prints the average
nos = raw_input("Enter numbers: ")
count=0
total=0
while nos != '':
	count=count + 1
	total=total + int(nos)
	nos = raw_input("Enter numbers: ")
	if nos == '':
		print 'Average is:',total/count
		print 'Do you want to repeat the process'
		ans= raw_input("Enter: ")
		if ans == 'y':
			nos = raw_input("Enter numbers: ")
		
		
			
