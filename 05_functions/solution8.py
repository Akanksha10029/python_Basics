# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
kwargs(name ="Akanksha",occupation = "student")

kwargs(name ="Akanksha",occupation = "student", enemy="Prashant")

#output:
# name: Akanksha
# occupation: student
# name: Akanksha
# occupation: student
# enemy: Prashant


# How Key-Value Pairs Work------>

# Key: The name of the argument (e.g., name, occupation, enemy).

# Value: The value assigned to the argument (e.g., "Akanksha", "student", "Prashant").

# When you call the function with kwargs(name="Akanksha", occupation="student"), Python automatically converts these arguments into a dictionary:

# {'name': 'Akanksha', 'occupation': 'student'}

# The for key, value in kwargs.items(): loop iterates through this dictionary, and the print(f"{key}: {value}") statement prints each key-value pair.