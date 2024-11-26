from Lab1.oven.oven_manager import OvenManager
from Lab3.observer.event_manager import EventManager

class OvenProxy:
    def __init__(self):
        self.oven_manager = OvenManager()
        self.pizzas_baked = 0
        self.is_locked = False
        self.event_manager = EventManager()

    def subscribe(self, observer):
        self.event_manager.subscribe(observer)

    def unsubscribe(self, observer):
        self.event_manager.unsubscribe(observer)

    def set_temperature(self, temp):
        if not self.is_locked:
            self.oven_manager.set_temperature(temp)
            self.event_manager.notify("TemperatureSet", {"temperature": temp})
        else:
            print("Access Denied: Oven is locked.")
            self.event_manager.notify("AccessDenied", {"action": "SetTemperature"})

    def start_baking(self, pizza_name):
        if not self.is_locked:
            self.oven_manager.start_baking(pizza_name)
            self.pizzas_baked += 1
            print(f"Baking started for: {pizza_name}")
            self.event_manager.notify("BakingStarted", {"pizza_name": pizza_name})
        else:
            print("Access Denied: Oven is locked.")
            self.event_manager.notify("AccessDenied", {"action": "StartBaking", "pizza_name": pizza_name})

    def stop_baking(self):
        if not self.is_locked:
            self.oven_manager.stop_baking()
            print("Baking stopped.")
            self.event_manager.notify("BakingStopped", {})
        else:
            print("Access Denied: Oven is locked.")
            self.event_manager.notify("AccessDenied", {"action": "StopBaking"})

    def take_your_pizza(self):
        if not self.is_locked:
            self.oven_manager.take_your_pizza()
            print("Pizza is ready to take!")
            self.event_manager.notify("PizzaReady", {})
        else:
            print("Access Denied: Oven is locked.")
            self.event_manager.notify("AccessDenied", {"action": "TakePizza"})

    def lock_oven(self):
        self.is_locked = True
        print("Oven locked.")
        self.event_manager.notify("OvenLocked", {})

    def unlock_oven(self):
        self.is_locked = False
        print("Oven unlocked.")
        self.event_manager.notify("OvenUnlocked", {})

    def get_baking_count(self):
        return self.pizzas_baked
