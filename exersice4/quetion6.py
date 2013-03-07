nos1 = int(raw_input("enter nb1"))
nos2 = int(raw_input("enter nb2"))
nos3 = int(raw_input("enter nb3"))
nos4 = int(raw_input("enter nb4"))
nos5 = int(raw_input("enter nb5"))

def sortsnumbers(n1,n2,n3,n4,n5):
	if n1>n2>n3>n4>n5:
		print n1
	elif n2>n1>n3>n4>n5:
		print n2
	elif n3>n1>n2>n4>n5:
		print n3
	elif n4>n1>n2<n3<n5:
		print n4
	elif n5<n1<n2<n3<n4:
		print n5
