#Write a function that accepts a single integer parameter, and returns a list of the prime numbers from 2 to the number
a=int(raw_input("Enter number: "))
listall=[]
def isprime(a):
	#return True if the number is prime, false otherwise
	if (a == 1) or (a == 2):
		return "is True"
	else : 
		for i in range(2, a ):
			if a%i == 0:
				return False

			return True
for i in range(2, a+1 ):
	if isprime(i) == True:
		listall = listall + [i]
print listall
