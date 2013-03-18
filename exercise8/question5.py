#Write a program that asks the user to enter a sequence of up to 5 x:y coordinates with both x and y in the range 0 to 4, ending their sequence entry by providing a blank line for the x coordinate. Then display a five by five grid of '#' characters, with the points in the grid entered by the user left blank. Assume x increases from left to right, and y increases from top to bottom.
i=1
l='#'
coordinate=[]
while i < 6:
	x=int(raw_input("Enter X : "))
	y=int(raw_input("Enter Y : "))
	coordinate=coordinate + [[x,y]]
	i=i+1
#x=2   y=1
print coordinate
for i in range(1,26):
	print l,
	if i%5 == 0:
		print ' '
	


