# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(p1,p2):
    return p1*p2

# print(multiply("Akanksha ","Prashant "))---> this will not work -> TypeError: can't multiply sequence by non-int of type 'str'
print(multiply(5,5))
print(multiply("Aadi ",3))
print(multiply(4,'Akanksha '))

#output--->
# 25
# Aadi Aadi Aadi
# Akanksha Akanksha Akanksha Akanksha
