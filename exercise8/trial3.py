x = int(raw_input("Enter x: "))
y = int(raw_input("Enter y: "))
i = 0
while i <25:
	if (x < 4) and (y < 4): 
		i= i + x + ((y*5)+1)
		if i==5:
			print " ",
			i=i+1
	else:
		print "#",
	if i%5 == 0:
		print ' '
