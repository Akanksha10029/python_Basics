# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a for and while loop.

num = int(input("Enter any number:"))
factorial = 1
for n in range(1,num+1):
    factorial *= n
print("The factorial of", num, "is", factorial)



number = int(input("Enter any number:"))
factorial = 1
original_number = number
while(number>0):
    factorial *= number
    number -= 1
print("The factorial of", original_number, "is", factorial)
