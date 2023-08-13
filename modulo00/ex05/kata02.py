# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

def adjust(a):
	if a < 10:
		return ('0' + str(a))

print(f"{adjust(kata[1])}/{kata[2]}/{kata[0]} {adjust(kata[3])}:{kata[4]}")