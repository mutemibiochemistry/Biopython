#(15%) Given the following list of nucleotide sequences, create a list of tuples where each tuple contains the number of A,T,G and C. (case insensitive)

nucleotides = [
	"tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
	"tttgggta",
	"tgactgtagcagtcaTATCGATG",
	"TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
	"ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]			#list of sequences
def count_nucleotides():						#function to count nucleotides
	lista = []					
	for sequence in nucleotides:
		counterA=0
		counterT=0
		counterG=0
		counterC=0
		for char in sequence:					#count occurence of each nucleotide
			if (char == 'A') or (char == 'a'):
				counterA=counterA + 1
			if (char == 'T') or (char == 't'):
				counterT=counterT + 1
			if (char == 'G') or (char == 'g'):
				counterG=counterG + 1
			if (char == 'C') or (char == 'c'):
				counterC=counterC + 1
		lista=lista + [(counterA,counterT,counterG,counterC)]	#store tuples of the count of each nucleotide per individual sequence
	return lista
print count_nucleotides()						#print list of tuples
