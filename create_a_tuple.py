# create a tuple
colors=("red", "green", "blue")
print(colors[0])
print(colors[2])
print(total_colors := len(colors))

#Check whether "Banana" exists in the tuple.
fruit=input("Enter a fruit name to check: ")
fruits = ("apple","banana","orange")
if fruit in fruits:
    print("fruit Found")
else:
    print("fruit not found")