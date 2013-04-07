#Software Description
#Your program should display a menu like the following and wait for the input of the user:
import projectoptions			#module containing validations of a PDB file
import textwrap
aminoacids=["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
aminoacidlet=["Ala","Arg","Asn","Asp","Cys","Glu","Gln","Gly","His","Ile","Leu","Lys","Met","Phe","Pro","Ser","Thr","Trp","Tyr","Val"]
d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K','ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N','GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R','TRP': 'W','ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
d2=dict((value,key) for key,value in d.items())			#interchange key-value in d
l='*'
s=' '
m="None    "


def sequence(sequence,numberperline,indentation=0):			#function to slice amino sequence to 50 characters
	seq=""
	index=0
	while index<len(sequence):
		if index == 0:
			seq = sequence[index:index+numberperline] + "\n"
			index +=numberperline
		else:
			seq += " "*indentation +sequence[index:index+numberperline] + "\n"
			index +=numberperline
	return seq


def menu():
	print 80*l,'\n',1*l,"PDB FILE ANALYZER",l.rjust(60),'\n',80*l,'\b\n',1*l,"Select an option from below:",l.rjust(49),'\b\n',1*l,l.rjust(78),'\b\n',1*l,4*s,"1) Open a PDB file",22*s,"(O)",l.rjust(27),'\b\n',1*l,4*s,"2) Information",26*s,"(I)",l.rjust(27),'\b\n',1*l,4*s,"3) Show histogram of amino acids",8*s,"(H)",l.rjust(27),'\b\n',1*l,4*s,"4) Display Secondary Structure",10*s,"(S)",l.rjust(27),'\b\n',1*l,4*s,"5) Manipulate Helix or Sheet",12*s,"(M)",l.rjust(27),'\b\n',1*l,4*s,"6) Export PDB File",22*s,"(X)",l.rjust(27),'\b\n',1*l,4*s,"7) Exit",33*s,"(Q)",l.rjust(27),'\b\n',1*l,l.rjust(78),'\b\n',1*l,52*s,"Current PDB: ",m,l.rjust(2),'\b\n',80*l
menu()
menuOption=raw_input(": ").upper()
while menuOption != "Q":
	if menuOption == 'O':
		path=raw_input("Enter a valid PATH for a PDB file: ")
		m=path
		print projectoptions.parsepdb(path)
		menu()
		m=path
		f = open(path, "r")


	if menuOption == 'I':
		title='Title:'
		sequenceA=[]
		listA=[]
		sequenceB=[]
		counterA=0
		counterB=0
		sequencechainA=''
		sequencechainB=''
		helixA=0
		helixB=0
		sheetA=0
		sheetB=0
		for line in f:

			if "HEADER" in line:
				Header= line[62:66]
			if "TITLE" in line:
				title=title + str(line[10:]).rstrip()
			if 'SEQRES' in line:
				if line[11] == 'A':
					sequenceA=sequenceA + line[19:70].strip('\n').rsplit(" ")
				if line[11] == 'B':
					sequenceB=sequenceB + line[19:70].strip('\n').rsplit(" ")
			if "HELIX" in line:
				if line[19] == 'A':
					helixA=helixA + 1
				if line[19] == 'B':
					helixB=helixB + 1
			if "SHEET" in line:
				if line[21] == 'A':
					sheetA=sheetA + 1
				if line[21] == 'B':
					sheetB=sheetB + 1
		listAA=''
		listBB=''
		for i in sequenceA:
			for key in d:
				if i == key:
					listAA=listAA + d[key]
					lenA=len(listAA)
		for i in sequenceB:
			for key in d:
				if i == key:
					listBB=listBB + d[key]
					lenB=len(listBB)
		lengthA=len(listAA)
		lengthB=len(listBB)
		a=sequence(listAA,50,14)
		b=sequence(listBB,50,14)				 
		print "PDB File: ",Header,".pdb",'\b\n',textwrap.fill(title,79),'\b\n',"CHAINS: A and B",'\b\n',"-  Chain A",'\b\n',"    Number of amino acids:",s,lengthA,'\b\n',"    Number of helix:",s*9,helixA,'\b\n',"    Number of sheet:",s*9,sheetA,'\b\n',"    Sequence:",a,'\n',"-  Chain B",'\b\n',"    Number of amino acids:",s*2,lengthB,'\b\n',"    Number of helix:",s*9,helixB,'\b\n',"    Number of sheet:",s*9,sheetB,'\b\n',"    Sequence: "+b,'\n',
		menu()


	if menuOption == 'H':
		f.seek(0)
		print "Choose an option to order by:",'\b\n',"number of amino acids - ascending  (an)",'\b\n',"number of amino acids - descending (dn)",'\b\n',"alphabetically - ascending         (aa)",'\b\n',"alphabetically - descending        (da)",'\b\n',
		aminoseq=listAA + listBB
		aminoseqlist=[]
		for i in range(len(aminoseq)):
			aminoseqlist=aminoseqlist + [aminoseq[i]]
		d={}
		a=0
		liststore=[]
		storedic={}
		for i in aminoacids:
			d[i]=aminoacidlet[a]
			a=a + 1
		for a in aminoseqlist:
			liststore=liststore + [d[a]]
			storedic[d[a]]=liststore.count(d[a])
		orderOption=raw_input("order by: ")
		newlist=storedic.items()
		if orderOption == 'an':								#lowest to highest nos of amino acids
			listofaminoacids=sorted(newlist,key=lambda x:(x[1]))
			for i in listofaminoacids:
				print i[0],"( "+ "%3s"% str(i[1])+")",":",i[1]*"*"
		if orderOption == 'dn':								#highest to lowest nos of amino acids
			listofaminoacids=sorted(newlist,key=lambda x:(x[1]))
			aminorev=listofaminoacids[::-1]
			for i in aminorev:
				print i[0],"( "+ "%3s"% str(i[1])+")",":",i[1]*"*"
		if orderOption == 'aa':								#alphabetically ascending
			listofaminoacids=sorted(newlist,key=lambda x:(x[0]))
			for i in listofaminoacids:
				print i[0],"( "+ "%3s"% str(i[1])+")",":",i[1]*"*"
		if orderOption == 'da':								#alphabetically descending
			listofaminoacids=sorted(newlist,key=lambda x:(x[0]))
			aminorev=listofaminoacids[::-1]
			for i in aminorev:
				print i[0],"( "+"%3s"% str(i[1])+")",":",i[1]*"*"
		f.seek(0)
		menu()


	if menuOption == 'S':
		f.seek(0)
		sequenceChainA=''
		sequenceChainB=''
		sheetlistA=[]
		sheetlistB=[]
		helixlist=[]
		helixidlist=[]
		sheetidlistA=[]
		sheetidlistB=[]
		listdashAA=''
		listdashBB=''
		dash='-'
		space=' '
		helix='/'
		sheet='|'
		tagID=''
		sheetIDA=''
		sheetIDB=''
		helixIDB=''
		helixid=''
		listAA=''
		listBB=''
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
				endchainID = line[31]
				helixtype = line[39]
				chainlen  = line[74:76]
				positionA = int(line[22:26].strip() + ' ')
				positionB = int(line[34:37].strip() + ' ')
				chainsubtype=line[13]
				helixlist += [[chaintype,helixnos,chainsubtype,positionA,positionB,helixtype,chainlen,endchainID]]
			if "SHEET" in line:
				chaintype=line[21]
				if chaintype == 'A':
					sheettype=line[9] + line[13]
					chainsubtype=line[13]
					positionA=int(line[23:26].strip() + ' ')
					positionB=int(line[34:37].strip() + ' ')
					strand=line[8:10]
					numStrands=line[14:16]
					initResName=line[17:20]
					endResName=line[28:31]
					endChainID=line[32]
					sense=line[38:40]
					curAtom=line[42]
					curResName=line[45:48]
					curChainId=line[49]
					curResSeq=line[51:54]
					prevAtom=line[57]
					prevResName=line[60:63]
					prevChainID=line[64]
					prevResSeq=line[66:69]
					prevICode=line[69]
					sheetlistA += [[chaintype,sheettype,chainsubtype,positionA,positionB,strand,numStrands,initResName,endResName,endChainID,sense,curAtom,curResName,curChainId,curResSeq,prevAtom,prevResName,prevChainID,prevResSeq,prevICode]]
				if chaintype == 'B':
					sheettype=line[9] + line[13]
					chainsubtype=line[13]
					positionA=int(line[23:26].strip() + ' ')
					positionB=int(line[34:37].strip() + ' ')
					strand=line[8:10]
					numStrands=line[14:16]
					initResName=line[17:20]
					endResName=line[28:31]
					endChainID=line[32]
					sense=line[38:40]
					curAtom=line[42]
					curResName=line[45:48]
					curChainId=line[49]
					curResSeq=line[51:54]
					prevAtom=line[57]
					prevResName=line[60:63]
					prevChainID=line[64]
					prevResSeq=line[66:69]
					prevICode=line[69]
					sheetlistB += [[chaintype,sheettype,chainsubtype,positionA,positionB,strand,numStrands,initResName,endResName,endChainID,sense,curAtom,curResName,curChainId,curResSeq,prevAtom,prevResName,prevChainID,prevResSeq,prevICode]]
		listA=[]
		listB=[]
		for i in sequenceA:
			for key in d:
				if i == key:
					listAA = listAA + d[key]
					positionsa=list(listAA)
					lenA=len(listAA)
					listdashAA=lenA*dash
					tagID=lenA*space
					sheetIDA=lenA*space
		for i in sequenceB:
			for key in d:
				if i == key:
					listBB = listBB  + d[key]
					positionsb=list(listBB)
					lenB=len(listBB)
					listdashBB=lenB*dash
					sheetIDB=lenB*space

		for j in helixlist:
			listdashAA=listdashAA[:j[3]-1] +  ((j[4]-j[3])+1)*helix + listdashAA[j[4]:]
			tagID=tagID[:j[3]-1] + j[1] + tagID[(j[3]-1+len(j[1])):]
		for j in sheetlistA:
			listdashAA=listdashAA[:j[3]-1] + ((j[4]-j[3])+1)*sheet + listdashAA[j[4]:]
			tagID=tagID[:j[3]-1] + j[1] + tagID[(j[3]-1+len(j[1])):]
		for j in sheetlistB:
			listdashBB=listdashBB[:j[3]-1] + ((j[4]-j[3])+1)*sheet + listdashBB[j[4]:]
			sheetIDB=sheetIDB[:j[3]-1] + j[1] + sheetIDB[j[3]:]
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
		print "Secondary Structure of the PDB id "+str(m[:4])+":",'\n',"Chain",chaintype+":",'\n',"("+helixtype+")"
		for i in range(0,nA):
			timesA=80*i
			for num in range(0+timesA,80+timesA):
				aminoa+=listAA[num]
				spacesA+=listdashAA[num]
				repA+=tagID[num]										
			print aminoa,'\n',spacesA,'\n',repA
			aminoa=''
			spacesA=''
			repA=''
		timesA=80*nA
		for i in range(0+timesA,remA+timesA):
			aminoa+=listAA[i]
			spacesA+=listdashAA[i]
			repA+=tagID[i]
		print aminoa,'\n',spacesA,'\n',repA,'\n',"("+str(lenA)+")",'\n',
		for i in range(0,nB):
			timesB=80*i
			for num in range(0+timesB,80+timesB):
				aminob+=listBB[num]
				spacesB+=listdashBB[num]
				repB+=sheetIDB[num]										
			print aminob,'\n',spacesB,'\n',repB
			aminob=''
			spacesB=''
			repB=''
		timesB=80*nB
		for i in range(0+timesB,remB+timesB):
			aminob+=listBB[i]
			spacesB+=listdashBB[i]
			repB+=sheetIDB[i]
		print aminob,'\n',spacesB,'\n',repB,'\n',"("+str(lenB)+")",'\n'
		menu()
		menuOption=raw_input(": ").upper()
		f.seek(0)

	if menuOption == 'M':
		p="\n"
		helixtype={1:'Right-handed alpha', 2:'Right-handed omega', 3:'Right-handed pi', 4:'Right-handed gamma', 5:'Right-handed 3 - 10', 6:'Left-handed alpha', 7:'Left-handed omega', 8:'Left-handed gamma', 9:'2 - 7 ribbon/helix', 10:'Polyproline'}  #conversion of numerical presentation of helix type
		d5 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K','ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N','GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R','TRP': 'W',	'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
		print "Choose one of the Manipulation Options:",p,"List(L)   Edit(E)   NEW(N)   REMOVE(R)   MAIN MENU(M)"
		man_option=raw_input("Enter manipulation option: ").upper()
		if man_option == "L":
			listoption = raw_input("Do you want to list the Helix (H) or the Sheet (S): ").upper()
			if listoption == "H":
				f.seek(0)
				for line in f:
					if "HELIX" in line:
						serNum      = line[9]
						helixID     = line[13]
						initResName = line[15:19]
						initChainID = line[19]
						initSeqNum  = line[22:26]
						initICode   = line[25]
						endResName  = line[27:30]
						endchainID  = line[31]
						endSeqNum   = line[34:37]
						endICode    = line[37]
						comment     = line[40:69]
						length      = line[74:76]
						helixClass  = line[39]
						if helixClass == "1":
							helixClass = "Right-handed alpha"
						elif helixClass == "2":
							helixClass = "Right-handed omega"
						elif helixClass == "3":
							helixClass = "Right-handed pi"
						elif helixClass == "4":
							helixClass = "Right-handed gamma"
						elif helixClass == "5":
							helixClass = "Right-handed 3 - 10"
						elif helixClass == "6":
							helixClass = "Left-handed alpha"
						elif helixClass == "7":
							helixClass = "Left-handed omega"
						elif helixClass == "7":
							helixClass = "Left-handed gamma"
						elif helixClass == "8":
							helixClass = "2 - 7 ribbon/helix"
						else:
							helixClass = "Polyproline"
						print "  SerNum:",serNum.rjust(6),p,"  helixID:",helixID.rjust(5),p,"  initResName:",initResName.rjust(1),p,"  initChainID:",initChainID,p,"  initSeqNum:",initSeqNum.rjust(1),p,"  initICode:",initICode.rjust(2),p,"  endResName:",endResName.rjust(2),p,"  endChainID:",endchainID.rjust(2),p,"  endSeqNum:",endSeqNum.rjust(4),p,"  endICode:",endICode.rjust(3),p,"  helixClass:",helixClass.rjust(5),p,"  comment:",comment.rjust(5),p,"  length:",length.rjust(7),p
			if listoption == "S":
				f.seek(0)
				for line in f:
					if "SHEET" in line:
						strand      = line[9:11]
						sheetID     = line[12:14]
						numStrands  = line[15:16]
						initResName = line[17:20]
						initChainID = line[21]
						initSeqNum  = line[23:26]
						initICode   = line[26]
						endResName  = line[28:31]
						endchainID  = line[32]
						endSeqNum   = line[34:37]
						endICode    = line[37]
						sense       = line[38:40]
						if sense == "1":
							sense = "parallel"
						elif sense == "-1":
							sense = "anti-parallel"
						curAtom     = line[41:43]
						curResName  = line[45:48]
						curChainID  = line[49]
						curResSeq   = line[51:54]
						curICode    = line[54]
						prevAtom    = line[57:59]
						prevResName = line[60:63]
						prevChainID = line[64]
						prevResSeq  = line[65:69]
						prevICode   = line[69]
						print "  strand:",strand.rjust(7),p,"  sheetID:",sheetID.rjust(5),p,"  numStrands:",numStrands.rjust(2),p,"  initResName:",initResName,p,"  initChainID:",initChainID,p,"  initSeqNum:",initSeqNum.rjust(2),p,"  initICode:",initICode.rjust(2),p,"  endResName:",endResName.rjust(4),p,"  endchainID:",endchainID.rjust(2),p,"  endSeqNum:",endSeqNum.rjust(5),p,"  endICode:",endICode.rjust(3),p,"  sense:",sense.rjust(7),p,"  curAtom:",curAtom.rjust(5),p,"  curResName:",curResName.rjust(4),p,"  curChainID:",curChainID.rjust(2),p,"  curResSeq",curResSeq.rjust(5),p,"  curICode:",curICode.rjust(2),p,"  prevAtom:",prevAtom.rjust(5),p,"  prevResName:",prevResName.rjust(2),p,"  prevChainID:",prevChainID.rjust(1),p,"  prevResSeq:",prevResSeq,p,"  prevICode:",prevICode.rjust(1),p
		if man_option == "E":
			editoption = raw_input("Do you want to edit a Helix (H) or the Sheet (S): ").upper()
			if editoption == "H":
				sequence=positionsa + positionsb
				helixoption=raw_input("Which Helix do you want to edit (1-"+str(len(helixlist)) + "):      ")
				helixlist[int(helixoption)-1][0]=raw_input(("  Chain")+helixlist[int(helixoption)-1][0]+": ")
				helixlist[int(helixoption)-1][3]=raw_input(("  initSeqNum")+str(helixlist[int(helixoption)-1][3])+": ")
				n=helixlist[int(helixoption)-1][3]
				print "That position correspond to the amino acid",d2[sequence[int(n)-1]]
				helixlist[int(helixoption)-1][4]=raw_input(("  endSeqNum")+str(helixlist[int(helixoption)-1][4])+":  ")
				e=helixlist[int(helixoption)-1][4]
				print "That position correspond to the amino acid",d2[sequence[int(e)-1]]
				helixlist[int(helixoption)-1][5]=raw_input(("  helixClass")+str(helixlist[int(helixoption)-1][5])+": ")
				h=helixlist[int(helixoption)-1][5]
				print "The selected class was:",helixtype[int(h)]
				comment=raw_input("  comment:         ")
				print "The Helix",helixoption,"has been successfully edited."

			if editoption == "S":
				sequence=positionsa + positionsb
				sheets=sheetlistA + sheetlistB
				sheetoption=raw_input("Which sheet do you want to edit (1-"+(str(len(sheets))) + "): ")
				sheets[int(sheetoption)-1][0]=raw_input(("  Chain type")+sheets[int(sheetoption)-1][0]+": ")
				sheets[int(sheetoption)-1][3]=raw_input(("  initSeqNum")+str(sheets[int(sheetoption)-1][3])+": ")
				n=sheets[int(sheetoption)-1][3]
				print "That position correspond to the amino acid",d2[sequence[int(n)-1]]
				sheets[int(sheetoption)-1][4]=raw_input(("  endSeqNum")+str(sheets[int(sheetoption)-1][4])+": ")
				e=sheets[int(sheetoption)-1][4]
				print "That position correspond to the amino acid",d2[sequence[int(e)-1]]
				comment=raw_input("  comment: ")
				print "The Sheet",sheetoption,"has been successfully edited."
		if man_option == "N":
			addoption = raw_input("Do you want to add a Helix (H) or a Sheet (S): ").upper()
			if addoption == "H":
				newlist=helixlist[0]
				helixlist=[newlist] + helixlist              #create a copy of list nos1 in the helix list which will be edited in subsquent steps
				sequence=positionsa + positionsb
				helixlist[0][0]=raw_input(("  Chain")+helixlist[0][0]+": ")
				helixlist[0][3]=raw_input(("  initSeqNum")+str(helixlist[0][3])+": ")
				n=helixlist[0][3]
				print "That position correspond to the amino acid",d2[sequence[int(n)-1]]
				helixlist[0][4]=raw_input(("  endSeqNum")+str(helixlist[0][4])+": ")
				e=helixlist[0][4]
				print "That position correspond to the amino acid",d2[sequence[int(e)-1]]
				helixlist[0][5]=raw_input(("  helixClass")+str(helixlist[0][5])+": ")
				h=helixlist[0][5]
				print "The selected class was:",helixtype[int(h)]
				comment=raw_input("  comment: ")
				print "The Helix",str(len(helixlist)),"has been successfully added."
			if addoption == "S":
				sequence=positionsa + positionsb
				sheets=sheetlistA + sheetlistB
				newsheet=sheets[0]
				sheets=[newsheet] + sheets		 #create a copy of list nos1 in the sheet list which will be edited in subsquent steps
				sheets[0][0]=raw_input(("  Chain type")+sheets[0][0]+": ")
				sheets[0][3]=raw_input(("  initSeqNum")+str(sheets[0][3])+": ")
				n=sheets[0][3]
				print "That position correspond to the amino acid",d2[sequence[int(n)-1]]
				sheets[0][4]=raw_input(("  endSeqNum")+str(sheets[0][4])+": ")
				e=sheets[0][4]
				print "That position correspond to the amino acid",d2[sequence[int(e)-1]]
				comment=raw_input("  comment:          ")
				print "The Sheet",str(len(sheets)),"has been successfully edited."
		if man_option == "R":
			p=' '
			sequence=positionsa + positionsb
			removeoption = raw_input("Do you want to remove a Helix (H) or a Sheet (S): ").upper()
			if removeoption == "H":
				helixoption=raw_input("Which Helix do you want to remove (1-"+str(len(helixlist)) + "): ")
				chainsubtype=helixlist[int(helixoption)-1][2]
				n=helixlist[int(helixoption)-1][3]
				initialseqname=d2[sequence[int(n)-1]]
				initID=helixlist[int(helixoption)-1][0]
				e=helixlist[int(helixoption)-1][4]
				endseqname=d2[sequence[int(e)-1]]
				endID=helixlist[int(helixoption)-1][7]
				chaintype=helixlist[int(helixoption)-1][5]
				chainlen=helixlist[int(helixoption)-1][6]
				print "Are you sure do you want to delete the helix?"
				print "HELIX   ",helixoption,p,chainsubtype,initialseqname,initID,p,n,p,endseqname,p,endID,p,e,chaintype,p,chainlen.rjust(32)
				confirm=raw_input("Y/N?: ").upper()
				if confirm == "Y":
					helixlist=helixlist.remove(helixlist[(int(helixoption)-1)])
					print helixlist
			elif removeoption == "S":
				sequence=positionsa + positionsb
				sheets=sheetlistA + sheetlistB
				print sheets
				sheetoption=raw_input("Which sheet do you want to remove (1-"+(str(len(sheets))) + "): ")
				sheetsubtype=sheets[int(sheetoption)-1][2]
				n=int(sheetoption)-1
				print n
				a=sheets[n][5]
				b=sheets[n][2]
				c=sheets[n][6]
				d=sheets[n][7]
				e=sheets[n][3]
				f=sheets[n][8]
				g=sheets[n][9]
				h=sheets[n][4]
				i=sheets[n][10]
				j=sheets[n][11]
				k=sheets[n][12]
				l=sheets[n][13]
				m=sheets[n][14]
				n=sheets[n][15]
		if man_option == "M":
			menu()
	if menuOption == "X":
		newpath=raw_input("File PATH: ")
		if ".pdb" not in newpath:
			print "Wrong file format"
		else:	
			newpath= open(newpath, "w")
			for line in f:
				newpath.write(line)
			print "FILE SAVED."
		action=raw_input("Press [enter] to go back to the menu. ")
		menu()
	elif menuOption == "Q":
		exitqtn=raw_input("Do you want to exit (E) or do you want to go back to the menu (M): ").upper()
		if exitqtn == "E":
			exit
		else:
			menu()
	menuOption=raw_input(": ").upper()

