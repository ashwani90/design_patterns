from abc import ABC
from enum import Enum
import auto
class HotDrink(ABC):
    def consume(self):
        pass
    
class Tea(HotDrink):
    def consume(self):
        print("this tea is delicious")
        
class Coffee(HotDrink):
    def consume(self):
        print("this coffee is delicious")
        
class HotDrinkFactory(ABC):
    def prepare(self, amoount):
        pass
    
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in a tea bag, boil water,'
              f' pour {amount}ml enjoy!')
        
        return Tea()
    
class CofeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water,'
              f'pout {amount}ml enjoy!')
        return Coffee()
    
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()
        
    factories = []
    initialized = False
    
    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
                
    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])
            s = input(f'Please pick drink (0-{len(self.factories)-1}):')
            idx = int(s)
            s = input(f'Specify amount: ')
            amount = int(s)
            return self.factories[idx][1].prepare(amount)
    
def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CofeeFactory().prepare(200)
    else:
        return None
    
if __name__ == '__main__':
    # entry = input("What kind of drink would you like?")
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()