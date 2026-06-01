import json
json_string ='{"name":"Keerthi","age":20,"city":"Hyderabad"}'
data=json.loads(json_string)
print(data["city"])

import json
a='"hloo"'
data=json.loads(a)
print(data)

import json
a="hloo"
data=json.dumps(a)
print(data)
