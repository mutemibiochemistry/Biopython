#Write a function that accepts a single integer parameter, and returns True if the number is prime, otherwise False.
a=int(raw_input("Enter number: "))
def isprime(a):
	#return True if the number is prime, false otherwise
	if (a == 1) or (a == 2):
		return "is True"
	else : 
		for i in range(2, a ):
			if a%i == 0:
				return str(a)+" is False"

		return str(a)+" is true"


print isprime(a)
