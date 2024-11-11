from abc import ABC, abstractmethod

class IngredientComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass
