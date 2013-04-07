#3 Show histogram of amino acids: This options allows to display a histogram based on the number of times an amino acid is in the sequence. For this option consider all the chains in the file as a single set. The user can choose to order the histogram by different methods. Example:
''': H
Choose an option to order by:
   number of amino acids - ascending  (an)
   number of amino acids - descending (dn)
   alphabetically - ascending         (aa)
   alphabetically - descending        (da)
order by: aa'''


menu_option=raw_input("Enter an option: ").upper()
if menu_option == 'H':
	print "Choose an option to order by:",'\b\n',"number of amino acids - ascending  (an)",'\b\n',"number of amino acids - descending (dn)",'\b\n',"alpphabetically - ascending        (aa)",'\b\n',"alphabetically - descending        (da)",'\b\n',"order by:"
orderOption=raw_input("Enter order option: ").upper()
aminoseq="YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRFSRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDDDELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRLSQDDIKGIQELYGASPDISYGNDALMP"
aminoseqlist=[]
for i in range(len(aminoseq)):
	aminoseqlist=aminoseqlist + [aminoseq[i]]
aminoacids=["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
aminoacidlet=["Ala","Arg","Asn","Asp","Cys","Glu","Gln","Gly","His","Ile","Leu","Lys","Met","Phe","Pro","Ser","Thr","Trp","Tyr","Val"]

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
orderOption=raw_input("Enter option: ")
newlist=storedic.items()
print newlist
if orderOption == 'an':
	listofaminoacids=sorted(newlist,key=lambda x:(x[1]))
	for i in listofaminoacids:
		print i[0],"(",i[1],":",i[1]*"*"
if orderOption == 'dn':
	listofaminoacids=sorted(newlist,key=lambda x:(x[1]))
	aminorev=listofaminoacids[::-1]
	for i in aminorev:
		print i[0],"(",i[1],":",i[1]*"*"
if orderOption == 'aa':
	listofaminoacids=sorted(newlist,key=lambda x:(x[0]))
	for i in listofaminoacids:
		print i[0],"(",i[1],":",i[1]*"*"
if orderOption == 'da':
	listofaminoacids=sorted(newlist,key=lambda x:(x[0]))
	aminorev=listofaminoacids[::-1]
	for i in aminorev:
		print i[0],"(",i[1],":",i[1]*"*"







