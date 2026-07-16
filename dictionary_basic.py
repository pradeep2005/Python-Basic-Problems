student ={
    "name":"Pradeep",
    "age":22,
    "department":"AI&DS"
    }
print(student)
print(student["name"])
print(student["age"])
print(student["department"])

#add a new item
student["cgpa"]=7.34
print(student)
student["age"]=23
print(student)
student.pop("age")
print(student)

#loop through the dictionary
for key,value in student.items():
    print(key,":",value)

print(student.keys())
print(student.values())
print(student.get("name"))

if "cgpa" in student:
    print("cgpa found")
else:
    print("cgpa not found")