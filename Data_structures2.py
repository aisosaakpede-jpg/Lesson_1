recipe1 = ("Waffle","5 mins","Easy")
recipe2 = ("Fried egg rice", "15 mins", "Moderate")

ingredient_for_recipe1 = {"flour","sugar","salt","egg","baking powder"}
ingredient_for_recipe2 = {"rice","salt","egg","soy sauce","ginger","msg"}

print(recipe1)
print(recipe2)

print(ingredient_for_recipe1.union(ingredient_for_recipe2))
print(ingredient_for_recipe1.intersection(ingredient_for_recipe2))
print(ingredient_for_recipe1.difference(ingredient_for_recipe2))
print(ingredient_for_recipe1.symmetric_difference(ingredient_for_recipe2))