class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not isinstance(name, str) or not name.strip():
			print("Invalid name value. It should be string.")
			exit()
		if not isinstance(cooking_lvl, int) or cooking_lvl > 5 or cooking_lvl < 1:
			print("Invalid cooking_lvl value. It should be an int between 1 and 5.")
			exit()
		if not isinstance(cooking_time, int) or cooking_time < 0:
			print("Invalid cooking_time value. It should be an positive int.")
			exit()
		if not isinstance(description, str):
			print('Invalid description. It should be a string.')
			exit()
		if isinstance(ingredients, list):
			for ing in ingredients:
				if not isinstance(ing, str):
					print('Invalid ingredient list.')
					exit()
		if recipe_type not in ["starter", "lunch", "dessert"]:
			print('Invalid recipe type. It should be "starter", "lunch" or "dessert".')
			exit()
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type	
	
	def __str__(self):
		txt = f"Recipe name: {self.name}\n"
		txt += f"Cooking level: {self.cooking_lvl}\n"
		txt += f"Cooking time: {self.cooking_time} minutes\n"
		txt += f"Ingredients: {' '.join(self.ingredients)}\n"
		txt += f"Description: {self.description}\n"
		txt += f"Recipe type: {self.recipe_type}\n"
		return txt
	