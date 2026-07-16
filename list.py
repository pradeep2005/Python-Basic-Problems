#list
names=["pradeep","kumar","prem"]
print(names)
#index
print(names[0])
print(names[1])
print(names[2])
#positive and negative
print(names[0])
print(names[-1])
print(names[-2])
#append
names.append("arun")
print(names)
#insert
names.insert(1,"aravind")
print(names)
#remove
names.remove("kumar")
print(names)
#pop
names.pop(0)
print(names)
#sort list
numbers=[5,2,8,1]
numbers.sort()
print(numbers)
#reverse
numbers.reverse()
print(numbers)
#len
print(len(names))
#for loop
for name in names:
    print(name)
