import math

def is_prime(item):
	for i in range(2,math.ceil(math.sqrt(item))+1):
		if item%i ==0 and item!=2:
			return False
	return True
	

item = 6

if is_prime(item):
	print('prime')
else:
	print('Composite')
