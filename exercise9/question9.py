#Write a program that reads a name and an age for a person, until the name is blank. Once all names have been present the user with an option to list the entered people in alphabetical order, or in descending age order. For either choice, list each person's name followed by their age on a single line. Make sure you output the correct age for the correct person

Name= raw_input("Enter name: ")
Age= int(raw_input("Enter age: "))
namelist=[]
while Name !='':
	age=int(Age)
	namelist=namelist + [[Name, age]]
	Name= raw_input("Enter name: ")
	Age= raw_input("Enter age: ")
question1= raw_input("Do you want to sort names or age, enter, age or name: ")
if question1 == 'name':
	namelist.sort()
if question1 == 'age':
	for i in namelist:
		i.reverse()
	namelist.sort()
print namelist
				
	
	
