import json


x = {
    "name":"john",
    "addr":"LA",
    "course":"java"
}

#convert to json
y = json.dumps(x)
print(type(y))

print(json.dumps(['car','computer','laptop']))
print(json.dumps(('car','mobile','books')))
print(json.dumps(50))
print(json.dumps(True))