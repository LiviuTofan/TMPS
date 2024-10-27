# pizza/factory.py
# Factory Method: PizzaFactory for creating pizzas

from pizza.Margherita import MargheritaPizza
from pizza.Pepperoni import PepperoniPizza
from pizza.Veggie import VeggiePizza

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type, size="medium"):
        if pizza_type == "Margherita":
            return MargheritaPizza(size)
        elif pizza_type == "Pepperoni":
            return PepperoniPizza(size)
        elif pizza_type == "Veggie":
            return VeggiePizza(size)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")