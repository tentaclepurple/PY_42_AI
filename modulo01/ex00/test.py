from recipe import Recipe
from book import Book

callos = Recipe(
name = 'callos',
cooking_lvl = 2,
cooking_time = 35,
ingredients = ['tripas', 'tomate', 'pimiento txorisero'],
description = '',
recipe_type = "lunch",
)

huevos_fritos = Recipe('huevos fritos', 1, 5, ['huevos', 'aceite', 'sal'], 'lo puto mejor', 'lunch')

mybook = Book("MyBook")

mybook.add_recipe(huevos_fritos)
mybook.add_recipe(callos)

print(mybook.get_recipes_by_types("lunch"))