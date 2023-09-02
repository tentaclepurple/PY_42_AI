import sys
def operations(a, b):
	try:
		print(f"Sum: {a + b}")
		print(f"Difference: {a - b}")
		print(f"Product: {a * b}")
		print(f"Quotient: {a / b}")
		print(f"Remainder: {a % b}")
	except ZeroDivisionError:
		print("Error. Division by 0")
	return

if len(sys.argv) == 1:
    sys.exit()
elif len(sys.argv) > 3 or len(sys.argv) < 3:
	print("Argument number error")
	sys.exit()
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
except ValueError:
    print("Both arguments must be integers.")
    sys.exit()
operations(a, b)
