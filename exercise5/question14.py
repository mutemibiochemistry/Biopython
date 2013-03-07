#14-enters solution
phrase1= raw_input("Enter phrase 1: ")
phrase2= raw_input("Enter phrase 2: ")
character= raw_input("Enter character: ")
counter1=0
counter2=0
nos=0
while nos < len(phrase1):
	if phrase1[nos] == character:
		counter1=counter1 + 1
	nos=nos + 1
print counter1
nos=0
while nos < len(phrase2):
	if phrase1[nos] == character:
		counter2=counter2 + 1
	nos=nos + 1
print counter2
if counter1 > counter2:
	print phrase1
elif counter2 > counter1:
	print phrase2

		

	
