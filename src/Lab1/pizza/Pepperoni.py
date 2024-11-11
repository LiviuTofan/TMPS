from Lab1.pizza.pizza_base import Pizza

class PepperoniPizza(Pizza):
    def __init__(self, size="medium"):
        super().__init__("Pepperoni", ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni"], size)

    def calculate_price(self):
        prices = {
            "small": 7.00,
            "medium": 9.00,
            "large": 12.00
        }
        return prices.get(self.size, 9.00)
