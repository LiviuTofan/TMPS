from abc import ABC, abstractmethod
import copy

class Pizza(ABC):
    def __init__(self, name, ingredients, size="medium"):
        self.name = name
        self.ingredients = ingredients
        self.size = size
        self.price = self.calculate_price()

    @abstractmethod
    def calculate_price(self):
        pass

    def prepare(self):
        print(f"Preparing {self.size.capitalize()} {self.name} pizza with ingredients:", ', '.join(self.ingredients))

    def clone(self):
        cloned_pizza = copy.deepcopy(self)
        cloned_pizza.price = cloned_pizza.calculate_price()
        cloned_pizza.ingredients = self.ingredients[:]
        return cloned_pizza
    
    def __str__(self):
        return f"{self.size.capitalize()} {self.name} Pizza (${self.price:.2f}) with ingredients: {', '.join(self.ingredients)}"
