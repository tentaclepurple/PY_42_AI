def text_analyzer(s = None):
	if s is None:
		s = input("Introduce a text: ")
	if type(s) != str:
		print("Argument is not a string")
		return
	l = 0
	u = 0
	point = 0
	space = 0
	print(f"The text contains {len(s)} character(s):")
	for i in s:
		if i.islower():
			l += 1
		elif i.isupper():
			u += 1
		elif i == ".":
			point += 1
		elif i == " ":
			space += 1
	print(f"- {l} lower letter(s)")
	print(f"- {u} upper letter(s)")
	print(f"- {point} punctuations mark(s)")
	print(f"- {space} space(s)")
 
if __name__ == "__main__":
	import sys
	if(len(sys.argv)) > 2:
		print("Argument number error")
		sys.exit()
	text_analyzer(sys.argv[1])