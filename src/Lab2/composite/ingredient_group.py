from Lab2.composite.ingredient_component import IngredientComponent

class IngredientGroup(IngredientComponent):
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def remove(self, ingredient):
        self.ingredients.remove(ingredient)

    def get_name(self):
        return self.name

    def get_cost(self):
        total_cost = sum(ingredient.get_cost() for ingredient in self.ingredients)
        return total_cost

    def __str__(self):
        ingredients_str = ", ".join(str(ingredient) for ingredient in self.ingredients)
        return f"{self.name} (Total: ${self.get_cost():.2f}): {ingredients_str}"
