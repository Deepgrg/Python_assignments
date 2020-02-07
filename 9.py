my_list = [23,12,523,23,234,32]

def tot_oc(item,my_list):
	newlist=[]
	for i in range(len(my_list)):
		if my_list[i] ==item:
			newlist.append(i)
	return newlist


result = tot_oc(23,my_list)
print(result)


		