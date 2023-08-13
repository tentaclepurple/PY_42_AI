cookbook = {
'Sandwich' : {
'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
'meal' : 'lunch',
'prep_time' : 10
},
'Cake' : {
'ingredients' : ['flour', 'sugar', 'eggs'],
'meal' : 'dessert',
'prep_time' : 60
},
'Salad' : {
'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
'meal' : 'lunch',
'prep_time' : 15
}
}

def print_recipe_names(dic):
    for i in dic.keys():
        print(i)

def print_rec_and_details(rec, dic):
	for i in dic.keys():
		if i == rec:
			print(f"{i}: ")
			for key, value in dic[i].items():
				if key == 'ingredients':
					print(f"ingredients: {', '.join(value)}")
				else:
					print(f"{key}: {value}")

def del_recipe(rec, dic):
    deleted = dic.pop(rec, None)
    if deleted == None:
        print("Recipe is not in Cookbook")
        
def add_recipe(dic):
    new_recipe = input("Enter a name for a new recipe: ")
    list_ingreds = []
    print("Enter one ingredient: ")
    while True:
        new_ingred = input("")
        if not new_ingred:
            break
        list_ingreds.append(new_ingred)
    meal_type = input("Enter a meal type: ")
    time = int(input("Enter a preparation time: "))
    new_inp = {
	'ingredients' : list_ingreds,
	'meal' : meal_type,
	'prep_time' : time
	}
    dic[new_recipe] = new_inp

while True:

    try:
        option = int(input("Enter an option: \n	1: Add a recipe\n	2: Delete a recipe\n	3: Print a recipe\n	4: Print the cookbook\n	5: Quit\n"))

        if option == 1:
            add_recipe(cookbook)
        elif option == 2:
            recipe = input("Enter a recipe name to get its details: ")
            print_rec_and_details(recipe, cookbook)
        elif option == 3:
            recipe = input("Enter a recipe name to get its details: ")
            print_rec_and_details(recipe, cookbook)
        elif option == 4:
            print(cookbook)
        elif option == 5:
            break
        else:
            print("Sorry, this option does not exist.")
    except ValueError:
        print("Invalid input. Try again")

