from pizza.pizza_base import Pizza

class CouponDecorator(Pizza):
    def __init__(self, pizza, discount=5.00):
        self.pizza = pizza
        self.discount = discount
        super().__init__(self.pizza.name, self.pizza.ingredients, self.pizza.size)

    def calculate_price(self):
        discounted_price = self.pizza.calculate_price() - self.discount
        if discounted_price < 0:
            return 0
        return discounted_price

    def prepare(self):
        self.pizza.prepare() 

    def __str__(self):
        return f"{self.pizza} (after coupon discount: -${self.discount:.2f})"
