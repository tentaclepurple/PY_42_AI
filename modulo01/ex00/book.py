from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name  #se inicia con el valor que recibe el constructor cuando se crea una instancia de Book
		self.creation_date = datetime.now()
		self.last_update = self.creation_date
		self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

	def add_recipe(self, recipe):
				#comprobar que lo que recibe el metodo add_recipe es una instancia/objeto de Recipe
		if not isinstance(recipe, Recipe):
			print("Error. Not an instance of Recipe.")
			return
				#en el atributo diccionario recipes_list, se añade con append la recipe recibida
				#en la key recipe_type adecuada (starter, lunch o dessert)
		self.recipes_list[recipe.recipe_type].append(recipe)
				#actualizamos last_update con el valor del tiempo actual
		self.last_update = datetime.now()

	def get_recipes_by_types(self, recipe_type):
		return [recipe.name for recipe in self.recipes_list[recipe_type]]
			#esta lista de comprension hace lo mismo que:
			#type_names = []
			#for recipe in self.recipes_list[recipe_type]:
			#	type_names.append(recipe.name)
			#return type_names

	def get_recipe_by_name(self, name):
		for recipe_type in self.recipes_list: #recorre keys del diccinario
			for recip in self.recipes_list[recipe_type]: #itera en cada receta
				if recip.name == name: #compara el nombre de la receta actual con el nombre que ha recibido como argumento
					print(f"You asked for the recipe {name}:")
					print(recip)
					return recip
		print(f"recipe '{name}' not found")
		return None