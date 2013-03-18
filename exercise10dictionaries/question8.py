#Write a program that reads in names until a blank line is entered, and prints out each unique name and the number of times it was entered.
Name= raw_input("Enter name: ")
names=[]
d={}

while Name != '':
	names = names + [Name]
	Name= raw_input("Enter name: ")
for i in list(names):
	d[i] = names.count(i)
print d
