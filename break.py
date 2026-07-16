#1
for i in range(1,11):
    if i==7:
        break
    print(i)
#2
for i in range (1,11):
    if i==5:
        continue
    print(i)
#3
a=input("enter the password:")

if a == "python123":
    print("Access granted")
else:
    print("access denied")
