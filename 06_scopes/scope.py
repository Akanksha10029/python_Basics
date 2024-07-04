def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

# Concept of Closure
# Closure: A closure is a function that "remembers" the environment (or scope) in which it was created, even after that environment is gone.

# Simplified Explanation-->
# When you create a function inside another function, the inner function can access variables from the outer function. Even if the outer function finishes execution and its local variables would normally be destroyed, the inner function still remembers those variables. This "remembering" is what we call a closure.



def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))

'''
Define the Outer Function chaicoder:
chaicoder is defined to take one argument num.
Inside chaicoder, another function actual is defined, which takes an argument x and returns x raised to the power of num.
chaicoder returns the function actual.
Create the Function f Using chaicoder(2):
f = chaicoder(2)
chaicoder is called with 2 as the argument.
Inside chaicoder, the function actual is created with num set to 2.
chaicoder returns the actual function.
f now holds a reference to this actual function where num is 2.
Create the Function g Using chaicoder(3):
g = chaicoder(3)
chaicoder is called with 3 as the argument.
Inside chaicoder, the function actual is created with num set to 3.
chaicoder returns the actual function.
g now holds a reference to this actual function where num is 3.
Call f(3) and Print the Result:
print(f(3))
f is called with 3 as the argument.
Inside f (which is the actual function returned by chaicoder(2)), x is 3 and num is 2.
The expression x ** num evaluates to 3 ** 2, which is 9.
The result 9 is printed.
Call g(3) and Print the Result:
print(g(3))
g is called with 3 as the argument.
Inside g (which is the actual function returned by chaicoder(3)), x is 3 and num is 3.
The expression x ** num evaluates to 3 ** 3, which is 27.
The result 27 is printed.


Closure in Action
The important part here is that actual function remembers the value of num from when chaicoder was called. This is the closure in action:

For f, num is 2.
For g, num is 3.
Even though chaicoder finished execution, the actual functions returned by it (stored in f and g) still have access to the num variable from their respective calls to chaicoder.
'''
