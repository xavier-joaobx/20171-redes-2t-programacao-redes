import json
f = open('pratica.json', 'r')
e = json.load(f)
print(e["author"])
