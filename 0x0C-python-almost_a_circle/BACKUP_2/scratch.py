import json
s = json.dumps({'name': 'Philip', 'age': 24})
print(s)
print(type(s))
my_dict = json.loads(s)
print(my_dict)
print(type(my_dict))
