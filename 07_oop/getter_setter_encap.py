class user:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name
    
    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be greater than 0")

user1 = user("Akanksha",20)
print(user1.get_name())
user1.set_name("Akanksha Rani")
print("New name of user1:",user1.get_name())

user1.set_age(19)
print("New age of user1:",user1.get_age())

user2 = user("Prashant",21)
print(user2.get_name())
user2.set_name("Prashant Sharma")
print("New name of user2:",user2.get_name())