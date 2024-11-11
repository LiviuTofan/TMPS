from Lab1.oven.oven_manager import OvenManager

class OvenProxy:
    def __init__(self):
        self.oven_manager = OvenManager()
        self.pizzas_baked = 0
        self.is_locked = False

    def set_temperature(self, temp):
        if not self.is_locked:
            self.oven_manager.set_temperature(temp)
        else:
            print("Access Denied: Oven is locked.")

    def start_baking(self, pizza_name):
        if not self.is_locked:
            self.oven_manager.start_baking(pizza_name)
            self.pizzas_baked += 1
            print(f"Baking started for: {pizza_name}")
        else:
            print("Access Denied: Oven is locked.")

    def stop_baking(self):
        if not self.is_locked:
            self.oven_manager.stop_baking()
        else:
            print("Access Denied: Oven is locked.")

    def take_your_pizza(self):
        if not self.is_locked:
            self.oven_manager.take_your_pizza()
        else:
            print("Access Denied: Oven is locked.")

    def lock_oven(self):
        self.is_locked = True
        print("Oven locked.")

    def unlock_oven(self):
        self.is_locked = False
        print("Oven unlocked.")

    def get_baking_count(self):
        return self.pizzas_baked
