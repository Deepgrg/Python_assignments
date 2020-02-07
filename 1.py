def is_sorted(item):
	for i in range(len(item)-1):
		if item[i]>item[i+1]:
			return False
	else:
		return True



eg= [2,4,5,6,7,10]	
print(is_sorted(eg))


