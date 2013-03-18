#Create a program that receive as many sequences as the user wants and calculates the GC ratio of each sequence. It should displays the sequences in order of its GC ratio, with the G's and C's in upper case and the T's and A's in lower case and in front of the sequence the calculated GC ratio. Finally it should show was the avarage GC ration among all the sequences.
nucleotides= raw_input("Enter sequences: ").lower()						#input sequence1 case insensitive as it will be converted to lower case
list1=[]											#list to store inputed strings of sequences
while nucleotides != '':									#while loop
	list1=list1 + [nucleotides]
	nucleotides= raw_input("Enter sequences: ").lower()
def count_nucleotides(list1):									#define function to count nucleotides
		lista = []
		nuc = ['a','c','g','t']								
		for sequence in list1:								#for loop
			counterA=0
			counterT=0
			counterG=0
			counterC=0
			counterX=0
			for char in sequence:							#count occurence of each nucleotide
				if char == 'a':
					counterA=counterA + 1
				if char == 't':
					counterT=counterT + 1
				if char == 'g':
					counterG=counterG + 1
				if char == 'c':
					counterC=counterC + 1
				if char not in nuc:
					counterX=counterX + 1
			lista=lista + [(counterA,counterT,counterG,counterC,counterX)]
		return lista
lista=count_nucleotides(list1)				
def gc_calculation(lista):									#function to calculate gc content
	gc_count=[]
	for i in lista:
		gc_count= gc_count + [(i[2] + i[3])/(1.0*(i[0] + i[1] + i[2] + i[3] + i[4]))]
	return gc_count
gc_count=gc_calculation(lista)
list2=[]
for i in list1:											#changing case of nucleotides
	i=i.replace('g','G') 
	i=i.replace('c','C')
	list2 = list2+[i]
gc_count,list2 = zip(*sorted(zip(gc_count, list2)))						#sort lists
for i in range (len(list2)):
	print list2[i],"\t","%5.3f" % (gc_count[i])						#print sequance and respective gc content in an ordered manner
gc_count=gc_calculation(lista)
average=0
for i in gc_count:
	average=average + i
	gcaverage=(average/(len(gc_count)))
print "AVERAGE GC RATIO =","%5.3f" % (gcaverage)						#calculae the average of GC of the different inputed sequences
