class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Test
d = Dog("Buddy", "Labrador")
d.bark()