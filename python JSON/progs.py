import json

data='{"fruit":"Apple","price":50}'
x=json.loads(data)
print(x)
#{'fruit': 'Apple', 'price': 50}

data={"fruit":"Apple","price":50}
x=json.dumps(data)
print(x)

