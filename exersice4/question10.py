name1 = raw_input("name1")
name2 = raw_input("name2")
name3 = raw_input("name3")

def printSortNames(n1,n2,n3):

	if n1<n2<n3:
		print n1,n2,n3
	
	elif n1<n3<n2:
		print n1,n3,n2
	elif n2<n3<n1:
		print n2,n3,n1
	elif n3<n2<n1:
		print n3,n2,n1
	else:
		print n3

printSortNames(name1, name2, name3)
