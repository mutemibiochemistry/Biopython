#Write a program that reads a name and an age for a person, until the name is blank. As each name age pair is entered, store names in a list, and ages in another. Print a list of tuples of paired names and ages.
Name= raw_input("Enter name: ")
Age= int(raw_input("Enter age: "))
namelist=[]
ageslist=[]
combined=[]
while (Name !='') and (Age != ''):
	age=int(Age)
	namelist=namelist + [Name]
	ageslist=ageslist + [age]
	Name= raw_input("Enter name: ")
	Age= raw_input("Enter age: ")
for value in range(len(namelist)):
	combined=combined + [[namelist[value]] + [ageslist[value]]]
	a=tuple(combined)
	
print a
