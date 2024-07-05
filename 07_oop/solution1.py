# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class car:
   def __init__(self, brand,model):
      self.brand = brand # self.brand--> class k andar k variable and only brand --> parameters which have been passed by the user during creation of object from the class
      self.model = model
my_car = car("Toyota","Maruti Suzuki")
print(my_car.brand)
print(my_car.model)


my_new_car = car("Tata","Safari")
print(my_new_car.brand)