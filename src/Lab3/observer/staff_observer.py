from Lab3.observer.observer import Observer

class StaffObserver(Observer):
    def update(self, event: str, data: dict):
        print(f"Staff Notification: {event} - {data}")
