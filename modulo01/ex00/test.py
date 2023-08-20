from recipe import Recipe
from book import Book
import time

callos = Recipe(
name = 'callos',
cooking_lvl = 2,
cooking_time = 35,
ingredients = ['tripas', 'tomate', 'pimiento txorisero'],
description = '',
recipe_type = "lunch",
)
print(callos)

""" 
huevos_fritos = Recipe('huevos fritos', 1, 5, ['huevos', 'aceite', 'sal'], 'lo puto mejor', 'lunch')

mybook = Book("MyBook")

mybook.add_recipe(huevos_fritos)
mybook.add_recipe(callos)

print(mybook.get_recipes_by_types("lunch"))
print()
#print(str(callos))

mybook.get_recipe_by_name("callos")
print()
mybook.get_recipe_by_name("tortilla")

print(mybook.creation_date)

time.sleep(30)

print(mybook.creation_date)
 """