# 8. Prime Number Checker
# Problem: Check if a number is prime.

num = int(input("Enter any number to check if it is prime or not:"))
is_prime = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
print(is_prime)