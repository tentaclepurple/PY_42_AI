from random import randint

class Character:
	def __init__(self, name):
		self.name = name
		self.life = 0
		self.attval = 0
		self.defval = 0

	def attack(self, foe):
		num = randint(0, 2)
		if num == 1 or num == 0:
			foe.life -= (self.attval + randint(0, 10)) - (foe.defval + randint(0, 10))
			if foe.life > 0:
				print(f"{foe.name} wounded. Life remaining: {foe.life}")
			else:
				print(f"{foe.name} is dead")
		else:
			print("Attack missed")
		
	def __str__(self):
		txt = f"{self.name} life: {self.life} "
		return txt

class Barbarian(Character):
	def __init__(self, name):
		super().__init__(name)
		self.type = "Barbarian"
		self.life = 50 + randint(0, 50)
		self.attval = 10
		self.defval = 5

class Amazon(Character):
	def __init__(self, name):
		super().__init__(name)
		self.type = "Amazon"
		self.life = 50 + randint(0, 50)
		self.attval = 5
		self.defval = 10
