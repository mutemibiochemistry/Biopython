#Write a program that outputs the position of every 't' in the list ['a', 'c', 'g', 't', 't', 'a', 't']. Use the index method, don't do it manually.
bases = ['a','c','g','t','t','a','t'] 		#list
for index in range(len(bases)):			#determine range
	if bases[index] =='t':			#condition
		print index,"->",bases[index]	#print
