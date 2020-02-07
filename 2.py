def is_anagrams(item1,item2):
	if len(item1)==len(item2):
		flag_1 = 0
		flag_2 = 0
		check = 0 
		for i in range(len(item1)):
			for letter in item2:
				if item1[i] == letter:
					flag_1+=1
		if flag_1 == len(item1):
			for i in range(len(item2)):
				for letter in item1:
					if item2[i] == letter:
						flag_2+=1
			if flag_2 == len(item2):
				return True
		else:
			return False
	else:
		return False



item1 = "ward"
item2 = "draw"

print(is_anagrams(item1,item2))