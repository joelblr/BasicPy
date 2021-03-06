#  --------------------------------------------------------------------------------------------------------------------------------130
#	Program to find the nth Fibonacci Number.

def fibo(n) :

	try :
		n = int(n)
		if n > -1 :
			if   n == 1 :	return (0)
			elif n == 2 :	return (1)
			a1, a2 = 0, 1
			for i in range(2, n) :
				s = a1 + a2
				a1, a2 = a2, s
			return (f"{n}th Number in Fibonacci Series : {a2}")
		else :	raise
	except :
		return(f"Plz Enter a Positive Integer!")

print(f"\n{'-'*130}\nFibonacci Series... 0 1 1 2 3 5 8...\n{'-'*130}\n")
n = input("Enter a Number : ")
print(f"{'>'*130}\n{fibo(n)}\n{'<'*130}\n")
#  --------------------------------------------------------------------------------------------------------------------------------130
#	Program to find If Number is Fibonacci Number.

def fiboCheck(n) :

	try :
		n = int(n)
		if n > -1 :
			if   n in [0, 1] :	return (f"{n} is a Fibonacci Number")
			a1, a2, s = 1, 1, 0

			while True :
				s = a1 + a2
				if   n  < s :	return (f"{n} is not a Fibonacci Number")
				elif n == s :	return (f"{n} is a Fibonacci Number")
				a1, a2 = a2, s


		else :	raise
	except :
		return(f"Plz Enter a Positive Integer!")


print(f"\n{'-'*130}\nFibonacci Series Check... 0 1 1 2 3 5 8...\n{'-'*130}\n")
n = input("Enter a Number : ")
print(f"{'>'*130}\n{fiboCheck(n)}\n{'<'*130}\n")
#  --------------------------------------------------------------------------------------------------------------------------------130
