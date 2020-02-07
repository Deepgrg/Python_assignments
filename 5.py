def is_palindrome(item):
	newitem=[]
	for i in range(len(item)-1,-1,-1):
		newitem.append(item[i])
	for j in range(len(item)):
		if item[j]!=newitem[j]:
			return False
	return True



item= "pop"

print(is_palindrome(item))