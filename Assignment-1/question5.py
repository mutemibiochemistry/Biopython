#5-print the multiplication table
i = 1					#multiplication variable
print "The Multiplication table:"	#print the multiplicationtable
while i < 11:				#set range
    n = 1
    while n <= 10:
        print "%2d" % (i * n),		#print 10 values by line spaced 2 spaces in between
        n += 1
    print ""				#print output
    i += 1

