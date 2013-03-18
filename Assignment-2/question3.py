#(10%) Extend the previous exercise to print your results in the next way: 
'''SEQUENCE 1: tcrgatgcajtcga
 A | 3 
-------
 T | 3 
-------
 G | 3 
-------
 C | 3 
-------
 * | 2 

SEQUENCE 2: CTAGTtatcatg
 A | 3 
-------
 T | 5 
-------
 G | 2 
-------
 C | 2 
-------
 * | 0 '''
nucleotides= raw_input("Enter sequences: ")										#Input sequences by user
list1=[]														#blank list to hold the sequences
while nucleotides != '':
	list1=list1 + [nucleotides]
	nucleotides= raw_input("Enter sequences: ")
def count_nucleotides(list1):												#function to count nucleotides
		lista = []
		nuc = ['a','c','g','t']
		for sequence in list1:											#counters of respective nucleotides
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
lista= count_nucleotides(list1)												#call function count_nucleotides
for elements in range(0,len(lista)):
	print "SEQUENCE", elements+1,":",list1[elements],"\n"," A","|",lista[elements][0],"\n","-------","\n"," T","|",lista[elements][1],"\n","-------","\n"," G","|",lista[elements][2],"\n","-------","\n"," C","|",lista[elements][3],"\n","-------","\n"," *", "|",lista[elements][4],"\n"		#print pattern where \n is an escape character for new line

