# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time of a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} seconds to execute")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)
example_func(2)