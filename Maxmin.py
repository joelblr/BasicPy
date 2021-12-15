#  --------------------------------------------------------------------------------------------------------------------------------130
#	Program to find Max/Min of given Numbers.

def max() :
	alist = [0]
	while True :
		try :	alist.append(float(input("Enter a Number : ")))
		except :	break
	alist.sort()
	return (alist[-1])

def min() :
	alist = [999999]
	while True :
		try :	alist.append(float(input("Enter a Number : ")))
		except :	break
	alist.sort()
	return (alist[0])

print(f"\n{'-'*130}\nMaximum Number Check\n{'-'*130}\n")
print(f"{'>'*130}\nMaximum Number : {max()}\n{'<'*130}")
print(f"\n{'-'*130}\nMinimum Number Check\n{'-'*130}\n")
print(f"{'>'*130}\nMinimum Number : {min()}\n{'<'*130}")
print(f"{'-'*130}\n")
#  --------------------------------------------------------------------------------------------------------------------------------130