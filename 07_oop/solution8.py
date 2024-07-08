# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class car:
    def __init__(self, name, model,color):
        self.__name = name
        self.__model = model
        self.__color = color

    @property
    def model(self):
        return self.__model
    @property
    def name(self):
        return self.__name
    @property
    def get_color(self):
        return self.__color.capitalize()
    
    
car1 = car("Tata","Safari","black")

car1.__color = "White"
print(car1.get_color)

car1.__name = "Toyota"
print(car1.name) # This line has no effect on the actual name attribute

car1.__model = "city" # This line has no effect on the actual __model attribute
print(car1.model) # city --> 'safari' changed to 'city' , but we want to make it non editable so make model as read only


# Explanation--->
# The @property decorator allows you to access methods as if they were attributes, which is more intuitive and enforces encapsulation.
# Using @property for both name and model ensures they are read-only and cannot be modified from outside the class.
# Directly accessing car1.__name or car1.__model creates new instance attributes and does not affect the private attributes defined in the class. This is due to name mangling in Python.
# In summary, using @property provides a cleaner and more controlled way to access private attributes while ensuring encapsulation and read-only properties.