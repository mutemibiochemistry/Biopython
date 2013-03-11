#7-determine a metropoly
city=raw_input("Enter city name: ")	
capital=raw_input("Enter Y or N: ")
popn=int(raw_input("Enter popn size: "))
income=raw_input("Enter average amount of income/per year: ")
i = 1
less=popn
lessname=city
largestincome=income
money=income
biggest=popn
biggestpopn=popn
while i <= 6:
	if (capital == 'Y' and popn > 100000) or (capital != 'y' and popn > 200000 and income >= 720000000):
		print city,"is a metropoly"
		if int(popn)<int(less):
			less=popn
			lessname=city
	else:
			if int(income)>int(money):
				money=income
				largestincome=city
	if (capital == 'Y'):
		if int(popn)>int(biggest):
			biggest=popn
			biggestpopn=city
	city=raw_input("Enter city name: ")		
	capital=raw_input("Enter Y or N: ")
	popn=int(raw_input("Enter popn size: "))
	income=raw_input("Enter average amount of income/per year: ")
	i = i + 1
	
print lessname
print largestincome
print biggestpopn
