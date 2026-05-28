#Add New Data to JSON
import json
student={"Name":"keerthi","roll":14}
student["course"]="CSM"
x=json.dumps(student)
print(x)