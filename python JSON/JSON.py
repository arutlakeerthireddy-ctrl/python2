#JSON in python:python has built-in package called json,which can be used to work with JSON data
#example
import json
#parse JSON - convert JSON to python
#if we have json string,we can parse it by using the json.loads() method
#example:convert json to python
import json
x='{"name":"keer","age":21,"city":"hyd"}'
y=json.loads(x)
print(y["city"])#hyd

#convert python to JSON
#if we have python object we can covert it into JSON string by using json.dumps() method
#example
import json
x={"Name":"uma","b":10,"clg":"gnu"}
y=json.dumps(x)
print(y)
#{"Name": "uma", "b": 10, "clg": "gnu"}

'''we can convert python objects like dict,list,tuple,string,int,float,True,False,None into JSON strings'''
#example
import json
print(json.dumps({"name":"keerthi","age":22}))
print(json.dumps([1,2,3,4]))
print(json.dumps((1,2,3,4,5)))
print(json.dumps("hlo"))
print(json.dumps(12))
print(json.dumps(56.8))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#example
import json

x = {
  "name":"John",
  "age":30,
  "married":True,
  "divorced": False,
  "children":("Ann","Billy"),
  "pets":None,
  "cars":[
    {"model":"BMW 230", "mpg": 27.5},
    {"model":"Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4,separators=(".","=")))
#output
'''{
    "name"="John".
    "age"=30.
    "married"=true.
    "divorced"=false.
    "children"=[
        "Ann".
        "Billy"
    ].
    "pets"=null.
    "cars"=[
        {
            "model"="BMW 230".
            "mpg"=27.5
        }.
        {
            "model"="Ford Edge".
            "mpg"=24.1
        }
    ]
}'''

#Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, sort_keys=True))
