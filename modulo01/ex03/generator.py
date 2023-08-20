import random

def get_random_list(size):
	n = 0
	list_rnd = []
	while n < size:
		num = random.randint(0, size - 1)
		if num not in list_rnd:
			list_rnd.append(num)
			n += 1
	return list_rnd

def generator(txt, sep=" ", option=None):
	if not isinstance(txt, str):
		print("ERROR")
		return
	lst = txt.split(sep)
	if option == 'unique':
		result = []
		for item in lst:
			if item not in result:
				result.append(item)
	elif option == 'ordered':
		result = sorted(lst)
	elif option == 'shuffle':
		result = [lst[idx] for idx in get_random_list(len(lst))]
	elif option == None:
		result = lst
	else:
		print("ERROR")
		return
	for item in result:
		yield item

if __name__ == '__main__':
	for item in generator("cagon tu tu tu puta calavera", ' ', 'shuffle'):
		print(item)
