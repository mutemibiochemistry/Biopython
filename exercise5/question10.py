#enters sequence of nos ending with a blank line then prints the average
nos = raw_input("Enter numbers: ")
count=0
total=0
while nos != '':
	count=count + 1
	total=total + int(nos)
	nos = raw_input("Enter numbers: ")
print 'Average is:',total/count
