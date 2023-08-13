from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name
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


"""	def get_recipe_by_name(self, name):
"""

		




