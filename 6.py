def gen_list(num1,num2):
	newlist=[]
	for i in range(num1+1,num2):
		newlist.append(i**2)

	return newlist


lst=gen_list(2,5)
print(lst)
