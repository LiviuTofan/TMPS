from Lab2.facade.order_facade import OrderFacade
from Lab1.factory.PizzaType import PizzaType
from Lab2.composite.ingredient_group import IngredientGroup
from Lab2.composite.available_ingredients import tomato, cheese, olives, mushrooms, pepperoni
from Lab2.proxy.oven_proxy import OvenProxy
from Lab3.observer.customer_observer import CustomerObserver
from Lab3.observer.staff_observer import StaffObserver

# Initialize the facade for pizza ordering and the oven proxy
order_facade = OrderFacade()
oven_proxy = OvenProxy()

# Add Observers
customer = CustomerObserver("John Doe")
staff = StaffObserver()
oven_proxy.subscribe(customer)
oven_proxy.subscribe(staff)

# Set oven temperature
oven_proxy.set_temperature(250)

# Order a large Margherita pizza with a $5 coupon
print("\nOrdering a large Margherita pizza with a $5 coupon:")
pizza, final_price = order_facade.order_pizza(PizzaType.MARGHERITA, size="large", discount=5.00)
oven_proxy.start_baking(pizza.name)
oven_proxy.stop_baking()
oven_proxy.take_your_pizza()
print(f"{pizza} is ready! Final price after discount: ${final_price:.2f}\n")

# Clone the Margherita pizza and modify the clone
print("Cloning and modifying the Margherita pizza by adding olives:")
cloned_margherita = pizza.clone()
cloned_margherita.ingredients.append("Olives")
print(f"Cloned pizza: {cloned_margherita}\nOriginal pizza: {pizza}\n")

# Order a small Pepperoni pizza without a discount
print("Ordering a small Pepperoni pizza without a discount:")
pepperoni_pizza, pepperoni_price = order_facade.order_pizza(PizzaType.PEPPERONI, size="small")
oven_proxy.start_baking(pepperoni_pizza.name)
oven_proxy.stop_baking()
oven_proxy.take_your_pizza()
print(f"{pepperoni_pizza} is ready! Final price: ${pepperoni_price:.2f}\n")

# Lock the oven and attempt to bake another pizza to demonstrate proxy control
oven_proxy.lock_oven()
print("Trying to bake with the oven locked:")
veggie_pizza, veggie_price = order_facade.order_pizza(PizzaType.VEGGIE, size="medium")
oven_proxy.start_baking(veggie_pizza.name)  # Should trigger "Access Denied"
oven_proxy.unlock_oven()

# Order a medium Veggie pizza with grouped ingredients
print("\nOrdering a medium Veggie pizza with grouped ingredients (Veggie Toppings):")
veggie_toppings = IngredientGroup("Veggie Toppings")
veggie_toppings.add(tomato)
veggie_toppings.add(cheese)
veggie_toppings.add(olives)
veggie_toppings.add(mushrooms)

veggie_pizza, veggie_price = order_facade.order_pizza(PizzaType.VEGGIE, size="medium")
oven_proxy.start_baking(veggie_pizza.name)
oven_proxy.stop_baking()
oven_proxy.take_your_pizza()
print(f"{veggie_pizza} is ready! Final price: ${veggie_price:.2f}")
print("Included Ingredients:", veggie_toppings)

# Payment using the Adapter pattern
print("\nProcessing payment for the Margherita pizza in EUR using Adapter pattern:")
from Lab2.domain.extern_payment_service import ExternalPaymentService
from Lab2.adapters.payment_adapter import PaymentAdapter

conversion_rate_usd_to_eur = 0.90
external_service = ExternalPaymentService()
payment_adapter = PaymentAdapter(external_service, conversion_rate=1 / conversion_rate_usd_to_eur)
payment_adapter.process_payment(final_price * conversion_rate_usd_to_eur, currency="EUR")

# Display Total Pizzas Baked
print("-" * 30)
print(f"Total pizzas baked: {oven_proxy.get_baking_count()}")
print("-" * 30)
