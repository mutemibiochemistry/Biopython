#x=2   y=1 i->8
#x=4   y=0 i->5
#x=3   y=0 i->4
#x=0   y=4 i->21
#x=0   y=3 i->16

#i== 
for i in range(1,26):
	if i==5:
		print " ",
	else:
		print "#",
	if i%5 == 0:
		print ' '

if x < 4 and y < 4:
	i= x + ((y*5)+1)

