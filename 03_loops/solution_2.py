# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter number:"))
sum_even = 0
even_num = []
for num in range(1,n+1):
    if num % 2 == 0:
        sum_even += 1
        even_num.append(num)
print("sum of even numbers:",sum_even)
print("Those Even numbers are:", even_num)