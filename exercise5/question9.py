#enters sequence of nos ending with a blank line then prints the smallest
nos = raw_input("Enter numbers: ")
smallest = nos
while nos != '':
	if int(nos) < int(smallest):		
		smallest = nos
	nos = raw_input("Enter numbers: ")
print smallest

