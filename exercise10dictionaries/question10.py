#A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner.

name=raw_input("Enter guest name: ").lower()
comment=raw_input("Enter guest comment: ")
guests={}
'''while name != 'quit':
	if name == 'show
	guests[name]=comment
	name=raw_input("Enter guest name: ").lower()
	print "name=",name
	if name == 'showcomments':
		print guests
	#comment=raw_input("Enter guest comment: ")
	if name in guests.keys():
		print guests[name]
		question = raw_input("Do you want to update previous comments: ")
		if question == 'y':
			updatecomment=raw_input("update guest comment: ")
			comment=updatecomment
		else:
			if question == '':
				break		
	else:
		comment=raw_input("Enter guest comment: ")
print guests'''

while name != 'quit':
	guests[name]=comment
	name=raw_input("Enter guest name: ").lower()
	if name == 'showcomments':
		for name,comment in guests.items():
			print name, comment
	comment=raw_input("Enter guest comment: ")			
	if name != 'quit':
		if name in guests.keys():
			print guests[name]
			question = raw_input("Do you want to update previous comments: ")
			if question == 'y':
				updatecomment=raw_input("update guest comment: ")
				comment=updatecomment
			else:
				if question == '':
					break		
	else:
		comment=raw_input("Enter guest comment: ")
print guests		

