# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter any number:"))
for n in range(1,11):
    if n == 5:
        continue
    print(f"{num} * {n} = {num*n}")