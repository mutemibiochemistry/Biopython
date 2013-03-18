#7a=d = {"Hitchhiker's Guide to the Galaxy": 1,"The Restaurant at the End of the Universe": 2,"Life, the Universe, and Everything": 3,"So Long, and Thanks for all the Fish!": 4,"Mostly Harmless": 5}
#7b= d["The Restaurant at the End of the Universe"]

'''d = {"Hitchhiker's Guide to the Galaxy": 1,"The Restaurant at the End of the Universe": 2,"Life, the Universe, and Everything": 3,"So Long, and Thanks for all the Fish!": 4,"Mostly Harmless": 5}
d = dict (zip(d.values(),d.keys()))
print d'''

d= {"Hitchhiker's Guide to the Galaxy": 1,"The Restaurant at the End of the Universe": 2,"Life, the Universe, and Everything": 3,"So Long, and Thanks for all the Fish!": 4,"Mostly Harmless": 5}
number= int(raw_input("Enter number: "))
for key in d:
	if d[key] == number:
		print key



