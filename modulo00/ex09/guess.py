import random
import sys


def ask():
	""" 
	Funcion para manejar la entrada del usuario 
	Si el usuario introduce un valor no númerico (o intro) se produce un 
	value error al intentar convertir en int y se devuelve None
	"""
	a = input("What's your guess between 1 and 99?\n")
	if a == 'exit':
		print("Goodbye")
		sys.exit()
	try:
		inp = int(a)
		return inp
	except ValueError:
		print("That's not a number.")
	return

def guess(num, inp):
		""" 
		Se compara la entrada del usuario con el valor random generado 
		"""
		if num > inp:
			print("Too low")
		if num < inp:
			print("Too high")
		if num == inp: 
			if num == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			elif num != 42 and tries != 1:
				print("Congratulations, you've got it!")
			if tries == 1:
				print("Congratulations! You got it on your first try!")
			else:
				print(f"You won in {tries} attempt(s)!")
			sys.exit()

num = random.randint(1, 99)
#num = 42
#print(num)
tries = 1

print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret number.')
print('Type "exit" to end the game.')
print('Good luck!')
print("\033[1;32mThis is an interactive guessing game!")
print("You have to enter a number between 1 and 99", end="")
print(" to find out the secret number.")
print("Type\033[0m \033[1;31m'exit'\033[0m \033[1;32mto end the game.")
print("\033[0m", end="")
print("\033[1;36mGood luck!\033[0m")
print()
""" 
bucle infinito hasta que se acierte o se escriba "exit"
"""
while True:
	inp = ask()
	if inp != None:
		guess(num, inp)
	tries += 1
	