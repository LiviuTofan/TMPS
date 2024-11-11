from Lab1.oven.oven_manager import OvenManager
from Lab1.factory.Factory import PizzaFactory
from Lab1.factory.Coupon import CouponDecorator
from Lab1.factory.PizzaType import PizzaType

class OrderFacade:
    def __init__(self):
        self.oven = OvenManager()
        self.factory = PizzaFactory()

    def order_pizza(self, pizza_type, size, discount=None):
        pizza = self.factory.create_pizza(pizza_type, size=size)
        pizza.prepare()

        if discount:
            pizza = CouponDecorator(pizza, discount=discount)
        
        self.oven.set_temperature(250)
        self.oven.start_baking(pizza.name)
        print(f"{pizza} is being baked!")
        self.oven.stop_baking()
        self.oven.take_your_pizza()
        
        final_price = pizza.calculate_price()
        return pizza, final_price
