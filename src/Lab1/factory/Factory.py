from Lab1.pizza.Margherita import MargheritaPizza
from Lab1.pizza.Pepperoni import PepperoniPizza
from Lab1.pizza.Veggie import VeggiePizza
from Lab1.factory.PizzaType import PizzaType

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: PizzaType, size="medium"):
        if pizza_type == PizzaType.MARGHERITA:
            return MargheritaPizza(size)
        elif pizza_type == PizzaType.PEPPERONI:
            return PepperoniPizza(size)
        elif pizza_type == PizzaType.VEGGIE:
            return VeggiePizza(size)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")