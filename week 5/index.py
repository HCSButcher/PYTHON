# assignment 1
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")


# Inheritance Example (Smartwatch inherits from Smartphone)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, strap_color):
        super().__init__(brand, model, price)  # call parent constructor
        self.strap_color = strap_color

    def track_steps(self):
        print(f"{self.brand} {self.model} is tracking your steps 🏃‍♂️")


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", 999)
phone1.call("123-456-789")
phone1.info()

watch1 = Smartwatch("Apple", "Watch 9", 399, "Black")
watch1.info()
watch1.track_steps()

# assignment 2

# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclasses with different move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
