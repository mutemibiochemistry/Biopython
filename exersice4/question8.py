year = raw_input("year1")
def leapyear(year1):
	if year1%4 == 0:
		print "leap year"
	else:
		print "not leap year"
test1 = leapyear(int(year))
