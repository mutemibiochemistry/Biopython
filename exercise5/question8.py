def lowerBase(base):
	if base == 'g' or base == 'G':
		return 'g'
	elif base == 'a' or base == 'A':
		return 'a'
	elif base == 't' or base == 'T':
		return 't'
	else:
		return 'c'
seq2 = ""
seq=raw_input("sequence: ")
counter = 0
while counter < len(seq):
	seq2 = seq2 + lowerBase(seq[counter])	
	counter = counter + 1

print seq2

