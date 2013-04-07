menuOption=raw_input("Enter menu option: ").upper()
sequenceChainA=''
sequenceChainB=''
sheetlistA=[]
sheetlistB=[]
helixlist=[]
helixidlist=[]
sheetidlistA=[]
sheetidlistB=[]
listdashAA=[]
listdashBB=[]
dash='-'
space=' '
helix='/'
sheet='|'
tagID=[]
sheetIDA=[]
sheetIDB=[]
helixIDB=[]
helixid=[]
f = open("/home/Thommas/mutemibiopython/mutemi2013miniproject/3AYU.pdb", "r")
listAA=''
listBB=''
if menuOption == 'S':
	for line in f:
		if "SEQRES" in line:
			sequenceChain= line[11]
			
			if sequenceChain == "A":
				sequenceChainA += line[19:].rstrip() + ' '
				sequenceChainA= sequenceChainA.replace(' ',',')
				sequenceA = sequenceChainA.split(",")
				
			else:
				sequenceChainB += line[19:].rstrip() + ' '
				sequenceChainB = sequenceChainB.replace(' ',',')
				sequenceB = sequenceChainB.split(",")
				
		if "HELIX" in line:
			helixnos = line[9]
			chaintype = line[19]
			positionA = int(line[22:26].strip() + ' ')
			positionB = int(line[34:37].strip() + ' ')
			chainsubtype=line[13]
			helixlist += [(chaintype,helixnos,chainsubtype,positionA,positionB)]
		if "SHEET" in line:
			chaintype=line[21]
			if chaintype == 'A':
				sheettype=line[9] + line[13]
				chainsubtype=line[13]
				positionA=int(line[23:26].strip() + ' ')
				positionB=int(line[34:37].strip() + ' ')
				sheetlistA += [(chaintype,sheettype,chainsubtype,positionA,positionB)]
			if chaintype == 'B':
				sheettype=line[9] + line[13]
				chainsubtype=line[13]
				positionA=int(line[23:26].strip() + ' ')
				positionB=int(line[34:37].strip() + ' ')
				sheetlistB += [(chaintype,sheettype,chainsubtype,positionA,positionB)]
d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K','ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N','GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R','TRP': 'W',	'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
listA=[]
listB=[]
for i in sequenceA:
	for key in d:
		if i == key:
			listAA = listAA + d[key]
			lenA=len(listAA)
			listdashAA=lenA*dash
			tagID=lenA*space
			sheetIDA=lenA*space
for i in sequenceB:
	for key in d:
		if i == key:
			listBB = listBB  + d[key]
			lenB=len(listBB)
			listdashBB=lenB*dash
			sheetIDB=lenB*space

for i in helixlist:
	listdashAA=listdashAA[:i[3]-1] +  ((i[4]-i[3])+1)*helix + listdashAA[i[4]:]
	tagID=tagID[:i[3]-1] + i[1] + tagID[(i[3]-1+len(i[1])):]
for i in sheetlistA:
	listdashAA=listdashAA[:i[3]-1] + ((i[4]-i[3])+1)*sheet + listdashAA[i[4]:]
	tagID=tagID[:i[3]-1] + i[1] + tagID[(i[3]-1+len(i[1])):]
for i in sheetlistB:
	listdashBB=listdashBB[:i[3]-1] + ((i[4]-i[3])+1)*sheet + listdashBB[i[4]:]
	sheetIDB=sheetIDB[:i[3]-1] + i[1] + sheetIDB[i[3]:]
aminoa=''
aminob=''
spacesA=''
spacesB=''
repA=''
repB=''
lenA=len(listAA)
lenB=len(listBB)
nA=lenA/80
nB=lenB/80
remA=lenA%80
remB=lenB%80
timesA=80
timesB=80
for i in range(0,nA):
	timesA=80*i
	for num in range(0+timesA,80+timesA):
		aminoa+=listAA[num]
		spacesA+=listdashAA[num]
		repA+=tagID[num]										
	print aminoa,'\n',spacesA,'\n',repA
	#print spacesA
	#print repA
	aminoa=''
	spacesA=''
	repA=''
timesA=80*nA
for i in range(0+timesA,remA+timesA):
	aminoa+=listAA[i]
	spacesA+=listdashAA[i]
	repA+=tagID[i]
print aminoa,'\n',spacesA,'\n',repA
print "("+str(lenA)+")"
for i in range(0,nB):
	timesB=80*i
	for num in range(0+timesB,80+timesB):
		aminob+=listBB[num]
		spacesB+=listdashBB[num]
		repB+=sheetIDB[num]										
	print aminob
	print spacesB
	print repB
	aminob=''
	spacesB=''
	repB=''
timesB=80*nB
for i in range(0+timesB,remB+timesB):
	aminob+=listBB[i]
	spacesB+=listdashBB[i]
	repB+=sheetIDB[i]
print aminob,'\n',spacesB,'\n',repB
print "("+str(lenB)+")"
print helixlist


	#print listBB
	#print listdashAA
	#print listdashBB
	#print tagID
	#print sheetIDB
