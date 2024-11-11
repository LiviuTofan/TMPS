from Lab1.pizza.pizza_base import Pizza

class VeggiePizza(Pizza):
    def __init__(self, size="medium"):
        super().__init__("Veggie", ["Tomato Sauce", "Mozzarella Cheese", "Mixed Vegetables"], size)

    def calculate_price(self):
        prices = {
            "small": 6.50,
            "medium": 8.50,
            "large": 11.50
        }
        return prices.get(self.size, 8.50)