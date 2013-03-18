#Write a program that accepts a list of numbers terminated by a blank line. Print out the entered numbers as elements of a tuple, in the order they were entered.

nos = int(raw_input("Enter number: "))
t = ()
while nos != '':
	v=int(nos)
	t = t + (v,)
	nos = raw_input("Enter number: ")
print t

