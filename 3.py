def remove_duplicate(item):
	newlist =[]
	for i in range(len(item)):
		if item[i] not in newlist:
			newlist.append(item[i])
	return newlist


lst = [1,2,4,2,4]
print(lst)
newlst=remove_duplicate(lst)
print(newlst)