#1
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a > b:
    print("first number is greater")
elif a<b:
    print("second number is greater")
else:
    print("Both are equal")

#2
mark=int(input("enter mark:"))

if mark >=90:
    print("grade A")
elif mark >=80:
    print("grade B")
elif mark >=70:
    print("grade C")
elif mark >=60:
    print("grade D")
else:
    print("fail")
