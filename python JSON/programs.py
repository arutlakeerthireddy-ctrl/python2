import json
json_string ='{"name":"Keerthi","age":20,"city":"Hyderabad"}'
data=json.loads(json_string)
print(data["city"])