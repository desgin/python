import json

celebrity = {"tom": dict(name="Tom",
                         address="1 red street, NY",
                         phone="123134"), "bob": dict(name="Bob",
                                                      address="9 pink street, NY",
                                                      phone="8998787")}
data = json.dumps(celebrity, ensure_ascii=False)
print(data)
with open("developer.json", "w") as f:
    f.write(data)
