import json

data='{"fruit":"Apple","price":50}'
x=json.loads(data)
print(x)
#{'fruit': 'Apple', 'price': 50}

data={"fruit":"Apple","price":50}
x=json.dumps(data)
print(x)

import json
data = {
    "name": "Keerthi",
    "age": 21,
    "city": "Suryapet"
}

json_data = json.dumps(data, indent=4)
print(json_data)

json_data = json.dumps(data, indent=4)
print(json_data)

