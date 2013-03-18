#(15%) Modify the previous code in such a way that the user can input as many sequences as he desires, and the tuples now have a 5th position that counts any other character different to a valid nucleotide. For example, if the user inputs 2 sequences: 
nucleotides= raw_input("Enter sequences: ")								#user enter  nucleotide sequences
list1=[]												#empty list to hold the inputed sequences
while nucleotides != '':
	list1=list1 + [nucleotides]
	nucleotides= raw_input("Enter sequences: ")
#print list1
def count_nucleotides(list1):										#function to count nucleotides
		lista = []
		nuc = ['a','c','g','t']
		for sequence in list1:									#nucleotide counters,where counterX is for any other characters
			counterA=0
			counterT=0
			counterG=0
			counterC=0
			counterX=0
			for char in sequence:
				if char.lower() == 'a':
					counterA=counterA + 1
				if char.lower() == 't':
					counterT=counterT + 1
				if char.lower() == 'g':
					counterG=counterG + 1
				if char.lower() == 'c':
					counterC=counterC + 1
				if char.lower() not in nuc:
					counterX=counterX + 1
			lista=lista + [(counterA,counterT,counterG,counterC,counterX)]
		return lista
print count_nucleotides(list1)										#call function
