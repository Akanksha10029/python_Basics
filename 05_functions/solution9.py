# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield(i)

for num in even_generator(10):
    print(num)

# In Python, yield is a keyword used in a function to make it a generator. When a function uses yield, it returns a generator object that can be iterated over, producing a sequence of values over time rather than computing and returning all the values at once.    


# Regular Function (with return):
# A regular function that returns a list of even numbers up to a limit would generate and store all the numbers in memory at once.
# Memory Usage: The list result contains all even numbers up to the limit, using a lot of memory.


# Generator Function (with yield):
# A generator function produces values one at a time, as needed, without storing the entire sequence in memory.
# Memory Usage: The generator produces one even number at a time and yields it. The number is processed, and then the generator continues to produce the next number, using much less memory.