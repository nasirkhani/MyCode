import json
#
# jn_str = "4"
# py_type = json.loads(jn_str)
#
# print(jn_str, type(jn_str))
# print(py_type, type(py_type))

with open("sample3.json",'r') as jf:
    str = json.load(jf)

print(str)
print(type(str))
