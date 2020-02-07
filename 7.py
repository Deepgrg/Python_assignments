num1=int(input("Enter a number"))
num2=int(input("Enter the divisor"))

def is_div(num1,num2):
	if num1%num2 ==0:
		return True
	return False

print(is_div(num1,num2))
