#Write a function that computes the sum of squares of two or three numbers.
a=int(raw_input("Enter number: "))
b=int(raw_input("Enter number: "))
c=raw_input("Enter number: ")

def addsquares(a,b,c=0):
	z = (a**2) + (b**2) + (c**2)
	return z

if c.isdigit():
	print addsquares(a,b,int(c))
else:
	print addsquares(a,b)

