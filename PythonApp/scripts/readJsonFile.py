import json 

with open('./PythonApp/data/fakeData.json') as f:
    data=json.load(f)
    print(data['records'][0])