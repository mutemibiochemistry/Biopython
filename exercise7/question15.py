height= raw_input("Enter height: ")
a = '*'
b = ' '
while height != '':
	for i in range(1,int(height)+1):
		print b*(int(height)-i)    +     a*i + a*(i-1)  +     b*(int(height)-i)
	for i in range(1,3):
		print b*(int(height)-1)    +     a*1
	height= raw_input("Enter height: ")
