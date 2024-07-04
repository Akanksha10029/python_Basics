# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    print("arguments are:", *args)
    print("Twice of arguments:", end = " ")

    for i in args:
        print(i*2, end=" ")
        
    print("\nsum:", end=" ")    
    # print(args)--> gives tuple
    return sum(args)
print(sum_all(1,2,3,4,5))

