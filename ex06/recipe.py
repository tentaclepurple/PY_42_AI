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



print_recipe_names(cookbook)
print()
print_rec_and_details('Salad', cookbook)