class GotCharacter:
	"""prueba1"""
	def __init__(self, first_name):
		self.first_name = first_name
		self.is_alive = True
	def print_stuff(self, stuff):
		print(stuff)

class Targaryen(GotCharacter):
	"""prueba2"""
	def __init__(self, first_name):
		super().__init__(first_name)
		self.family_name = 'Targaryen'
		self.house_words = 'Fire and blood'
	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

aegon = Targaryen("Aegon")
print(aegon.first_name)
print(aegon.__doc__)
print(aegon.is_alive)
aegon.die()
print(aegon.is_alive)
aegon.print_house_words()
aegon.print_stuff("Dracarys!!")
