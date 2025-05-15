class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()

# Test
car = Car()
car.start()
