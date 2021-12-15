#  --------------------------------------------------------------------------------------------------------------------------------130
#	Python Program to evaluate Factorial of a given Number

def factorial(n) :

	try :
		f, n = 1, int(n)
		if not n > -1  :  raise
		if n in [0, 1] :	return 1
		f = f * n * factorial(n-1)
		return (f)

	except : return (False) #	return ("Error")

f = 1
while f :
	f = factorial(input(f"\n{'-'*130}\nEnter A Number : "))
	print(f"Factorial      : {f}\n{'-'*130}")
print()
#  --------------------------------------------------------------------------------------------------------------------------------130