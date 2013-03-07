nos1 = int(raw_input("enter nos: "))
nos2 = int(raw_input("enter nos: "))
b = 0
if nos2<nos1:
	while nos2 <= nos1:
		b = b + nos2
		nos2=nos2+1
else:
	while nos1 <= nos2:
		b = b + nos1
		nos1=nos1 + 1
print b
	

