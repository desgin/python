import json
with open('developer.json') as json_file:
    data = json.load(json_file)
print(data)