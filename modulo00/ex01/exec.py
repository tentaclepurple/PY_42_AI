import sys

list = sys.argv
str = ' '.join(list[1:])
inv = str[::-1]
strf = ""
for i in inv:
    if i.isupper():
        strf += i.lower()
    else:
    	strf += i.upper()

print(strf)