import json
f = open("developer.json", "r")
s = f.read()
celebrity = json.loads(s)
print(celebrity)
