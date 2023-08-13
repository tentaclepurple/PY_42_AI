import sys

if len(sys.argv) != 2:
    print("Argument different from 1")
    sys.exit()

try:
	i = int(sys.argv[1])
except:
    print("Argument is not an int")
    sys.exit()

if i == 0:
    print("I´m zero")
elif i % 2 == 0:
    print("I´m even")
elif i % 2 != 0:
	print("I´m odd")


    