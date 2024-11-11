from Lab1.pizza.pizza_base import Pizza

class MargheritaPizza(Pizza):
    def __init__(self, size="medium"):
        super().__init__("Margherita", ["Tomato Sauce", "Mozzarella Cheese", "Basil"], size)

    def calculate_price(self):
        prices = {
            "small": 6.00,
            "medium": 8.00,
            "large": 11.00
        }
        return prices.get(self.size, 8.00)
