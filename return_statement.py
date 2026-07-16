#1
def add(a, b):
    return a+b
sum=add(10,20)
print(sum)
#2

def cube(num):
    return num ** 3
cube1=cube(3)
print(cube1)
#3
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))
print(is_even(7))