m=int(raw_input("Enter m: "))							#prompt user from user
b=int(raw_input("Enter b: "))							#prompt user from user
print "The results for the linear equation Y=mX+b with m=",m,"and b=",b,"are:"	#print title
print "X","\t","Y"								#print header titles
if m != ' ':									#exclude space from equation
	for X in range(1,11):							#determine range of operation
		Y=m*X + b							#operation formula
		print X,"\t",Y							#print output
