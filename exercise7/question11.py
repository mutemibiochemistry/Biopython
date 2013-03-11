nos = raw_input("Enter number: ")
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
dates = ['31','28','31','30','31','30','31','31','30','31','30','31']
nos = int(nos)-1
for i in range(len(months)):
	if i == nos:
		for k in range(len(dates)):
			if i == k:
				print months[i],"has",dates[k], "days."
