import sys
import re

if len(sys.argv) != 3:
	print("Error")
	exit()
try:
	s = str(sys.argv[1])
	n = int(sys.argv[2])
except ValueError:
	print("Type Error")
	exit()

clean_list = re.findall(r'\b\w+\b', s)

output = [word for word in clean_list if len(word) >= n]
print(output)