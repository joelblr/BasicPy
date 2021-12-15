#  --------------------------------------------------------------------------------------------------------------------------------130
#	Program to check if given Number is Prime or not.

def prime(n) :

	try :
		n = int(n)
		if n > 0 :
			if n == 1 :	return (f"{'>'*130}\n{n} is not a Prime Number\n{'<'*130}")
			for i in range(int(n**0.5), 1, -1) :
				if n % i == 0 :	return (f"{'>'*130}\n{n} is not a Prime Number\n{'<'*130}")
			return (f"{'>'*130}\n{n} is a Prime Number\n{'<'*130}")
		else :		raise
	except Exception as e :
		return (f"{'>'*130}\nPlz Enter a Positive Integer!\n{'<'*130}")

print(f"\n{'-'*130}")
print(prime(input("Enter a Number : ")))

#  --------------------------------------------------------------------------------------------------------------------------------130
#	Program to check if given Numbers are Prime in the given Interval [a,b].

def primeCheck(l) :

	try :
		if not l : l = "1,10"
		l = list(map(int, l.split(",")))
		if not (l[0] > 0 and l[1] > 0) :	raise
		print(f"{'>'*130}\nPrime Numbers in Interval {l}\n")
		for n in range(l[0], l[-1]+1) :
				if n in [0, 1] :	continue
				flag = True
				for i in range(int(n**0.5), 1, -1) :
					if n % i == 0 :	
						flag = False
						break
				if flag :
					print(f"{n}")
	except :
		print (f"{'>'*130}\nPlz Enter a Positive Integer!")
	finally :
		print(f"{'<'*130}\n")

print(f"\n{'-'*130}")
l = input("Enter Start,Stop Value : ")
primeCheck(l)
#  --------------------------------------------------------------------------------------------------------------------------------130