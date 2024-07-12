"""
loads -> json string to python type ----> deserialize
load -> json file to python type

dumps -> python type to json string ----> serialize
dump -> python type to json file
"""
import json

#
# jn_str = "4"
# py_type = json.loads(jn_str)
#
# print(jn_str, type(jn_str))
# print(py_type, type(py_type))

# with open("sample3.json",'r') as jf:
#     str = json.load(jf)
#
# print(str)
# print(type(str))

# name = "reza"
# age = 25
# marks = {"riazi": [15, 16, 17], "fizik": [20, 19, 9]}
# lessons = ["fizik", "honar", "riazi"]
# b = False
#
# p = {"name": name, "age": age, "marks": marks, "lessons": lessons, "b": b}

# with open("myfile.json", "w") as jf:
#     json.dump(p, jf, indent=4)


with open("myfile.json") as pf:
    p = json.load(pf)

name = p["name"]
age = p["age"]
marks = p["marks"]
lessons = p["lessons"]
b = p["b"]

print(name)
print(age)
print(marks)
print(lessons)
print(b)
