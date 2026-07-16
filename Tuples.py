# create a tuple
colors=("red", "green", "blue")
print(colors[0])
print(colors[2])
print(total_colors := len(colors))


#tuple Print all numbers using a for loop.
numbers = (10, 20, 30, 40, 50)
for num in numbers:
    print(num)

#Check whether "Banana" exists in the tuple.
fruit=input("Enter a fruit name to check: ")
fruits = ("apple","banana","orange")
if fruit in fruits:
    print("fruit Found")
else:
    print("fruit not found")