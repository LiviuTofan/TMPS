
# Main file to demonstrate usage of the Singleton, Factory Method, Prototype and Decorator patterns

from oven.oven_manager import OvenManager
from factory.Factory import PizzaFactory
from factory.Coupon import CouponDecorator

oven = OvenManager()
oven.set_temperature(250)

factory = PizzaFactory()

# Create a large Margherita pizza
margherita_large = factory.create_pizza("Margherita", size="large")
margherita_large.prepare()
oven.start_baking(margherita_large.name)
print(margherita_large, "is ready to serve!")
oven.stop_baking()
oven.take_your_pizza()

# Use the 5$ coupon on the large Margherita pizza, by implementing the Decorator pattern
coupon_discount = 5.00
margherita_with_coupon = CouponDecorator(margherita_large, discount=coupon_discount)
print(margherita_with_coupon)
final_price = margherita_with_coupon.calculate_price()
print(f"Final price after coupon: ${final_price:.2f}") 
print()

# Clone the large Margherita pizza and modify the clone by adding an ingredient and changing the size using the Prototype pattern
cloned_margherita = margherita_large.clone()
cloned_margherita.ingredients.append("Olives")
cloned_margherita.size = "medium"
print(cloned_margherita)  # Now reflects the new size and ingredients
print(margherita_large)   # Original pizza remains unchanged
print()

pepperoni_small = factory.create_pizza("Pepperoni", size="small")
pepperoni_small.prepare()
oven.start_baking(pepperoni_small.name)
print(pepperoni_small)
oven.stop_baking()
oven.take_your_pizza()

veggie_medium = factory.create_pizza("Veggie", size="medium")
veggie_medium.prepare()
oven.start_baking(veggie_medium.name)
print(veggie_medium)
oven.stop_baking()
oven.take_your_pizza()