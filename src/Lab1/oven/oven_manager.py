class OvenManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OvenManager, cls).__new__(cls)
            cls._instance.temperature = 200
            cls._instance.is_occupied = False
        return cls._instance

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"Oven temperature set to {self.temperature}°C.")

    def start_baking(self, pizza_name):
        if not self.is_occupied:
            print(f"Baking {pizza_name} pizza at {self.temperature}°C.")
            self.is_occupied = True
        else:
            print("Oven is currently occupied!")

    def stop_baking(self):
        if self.is_occupied:
            print("Baking finished. Oven is now free.")
            self.is_occupied = False
        else:
            print("Oven is already free.")

    def take_your_pizza(self):
        print("-" * 30) 
        print("TAKE YOUR PIZZA!") 
        print("-" * 30) 