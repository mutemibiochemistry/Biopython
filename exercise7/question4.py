nos = raw_input("Enter number: ")
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
nos = int(nos)-1
for i in range(len(months)):
	if i == nos:
		print months[i]
