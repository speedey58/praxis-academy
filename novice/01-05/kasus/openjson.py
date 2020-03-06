import json

file_json = open('profiles.json')
data=json.loads(file_json.read())

print(data)
