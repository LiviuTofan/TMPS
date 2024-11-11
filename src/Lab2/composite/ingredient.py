from Lab2.composite.ingredient_component import IngredientComponent

class Ingredient(IngredientComponent):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def __str__(self):
        return f"{self.name} (${self.cost:.2f})"