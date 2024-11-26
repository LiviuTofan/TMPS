from Lab3.observer.observer import Observer

class CustomerObserver(Observer):
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def update(self, event: str, data: dict):
        print(f"Notification for {self.customer_name}: {event} - {data}")
