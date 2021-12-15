#  ------------------------------------------------------------------------------------------------------------------------------------------140
#	Program to Perform Basic Maths

def add(x, y) :
	return (x+y)

def sub(x, y) :
	return (x-y)

def multi(x, y) :
	return (x*y)

def div(x, y) :
	if y != 0 :	return (str(x/y)[:str(x/y).index(".")+4])
	return ("<Error : Division By 0>")

while True :

	operator = input(f"\n{'-'*130}\nEnter Operator : ")
	if operator not in ["*", "/", "+", "-"] :	break
	number_1 = int(input("Enter Number 1 : "))
	number_2 = int(input("Enter Number 2 : "))

	if   operator == '*' :	print(f"{'>'*130}\nResult : {number_1} {operator} {number_2} = {multi(number_1, number_2)}\n{'<'*130}\n{'-'*130}")
	elif operator == '/' :	print(f"{'>'*130}\nResult : {number_1} {operator} {number_2} = {div(number_1, number_2)}\n{'<'*130}\n{'-'*130}")
	elif operator == '+' :	print(f"{'>'*130}\nResult : {number_1} {operator} {number_2} = {add(number_1, number_2)}\n{'<'*130}\n{'-'*130}")
	elif operator == '-' :	print(f"{'>'*130}\nResult : {number_1} {operator} {number_2} = {sub(number_1, number_2)}\n{'<'*130}\n{'-'*130}")
print(f"{'-'*130}\n")
#  ------------------------------------------------------------------------------------------------------------------------------------------140