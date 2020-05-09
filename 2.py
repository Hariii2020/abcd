import json

with open('details.json')as json_file:
    json_object=json.load(json_file)

print(json_object)

print(json.dumps(json_object))

print(json.dumps(json_object,indent=2))