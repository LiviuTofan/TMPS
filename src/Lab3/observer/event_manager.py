from Lab3.observer.subject import Subject

class EventManager(Subject):
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, event: str, data: dict):
        for observer in self._observers:
            observer.update(event, data)
