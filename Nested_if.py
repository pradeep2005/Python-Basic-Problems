#1
age=int(input("enter age:"))
degree=input("enter degree:")

if age >=18:
    if degree=="b.tech":
        print("eligible for interview")
    else:
        print("not eligible degree")
else:
    print("not eligible age")
#2

year=int(input("enter year:"))
if year % 4==0:
    print("leap year")
else:
    print("not leap year")
