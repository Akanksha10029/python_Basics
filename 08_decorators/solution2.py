# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, args, kwargs)
        if not args:
            args_value = "0 args"
        else:
            args_value = ", ".join([str(arg) for arg in args])
        if not kwargs:
            kwargs_value = "0 kwargs"
        else:
            kwargs_value = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling: {func.__name__} with args and kwargs({args_value}, {kwargs_value})")
        return func(*args,**kwargs)
    return wrapper
@debug
def hello():
    print("Hello World")

@debug
def greet(name,greeting="Hanji",punctuation="."):
    print(f"{greeting} {name} {punctuation}")

greet("Chai",greeting="Hello",punctuation="!")
hello()