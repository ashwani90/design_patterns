import random
class Database:
    _instance = None
    def __init__(self):
        id = random.randint(1,101)
        print('id = ', id)
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls,*args,**kwargs)
            return cls._instance
        
class Database2:
    def __init__(self):
        print("Loading Database")
        
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1==d2) # sample implementation
    d1 = Database2()
    d2 = Database2()
    print(d1==d2)
    
def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args,**kwargs)
            return instances[class_]
    return instances

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
