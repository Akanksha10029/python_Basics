# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    @staticmethod # decorator   
    def general_description():
        return "Cars are very awesome"
car1 = car("Tata","Lavender","10L")
print(car1.price)
print(car.general_description())
# print(car.name)--> AttributeError: type object 'car' has no attribute 'name'