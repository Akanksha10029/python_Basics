# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class car:
    def __init__(self,brand,model):
        self.__brand = brand # making brand private by inserting __in starting of brand variable/attribute (__brand)
        self.model = model
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
my_car = car("Toyota","corolla")

# print(my_car.brand) --> direct brand is not accessible as due to __brand (private)---> AttributeError: 'car' object has no attribute 'brand'

# print(my_car.__brand) --> AttributeError: 'car' object has no attribute '__brand'. Did you mean: 'get_brand'?

# we can access those private attributes only inside the class car but object can not access it. so if we want to access it then we have to make methods/functions i.e [get_] get_brand

print(my_car.get_brand()) # Toyota!