#Write a program that accepts a list of numbers terminated by a blank line, and stores the result in a tuple, a. Repeat the process to form a second user inputted tuple, b, making sure there are the same number of elements in b as in a. Print out the result of the mathematical addition (not concatenation) of the two tuples as a tuple.
nos = int(raw_input("Enter number: "))
a = ()
while nos != '':
	v=int(nos)
	a = a + (v,)
	nos = raw_input("Enter number: ")

nos = int(raw_input("Enter number: "))
b = ()
while nos != '':
	u=int(nos)
	b = b + (u,)
	nos = raw_input("Enter number: ")
if len(a) == len(b):
	total = map(sum, zip(a,b))
	print total
else:
	print " a != b"
		
	

