from faker import Faker 
import json 

output=open('./PythonApp/data/fakeData.json','w')
fake=Faker()

allData={}
allData['records']=[]
for i in range(1000):
    data={"name":fake.name(),"age":fake.random_int(min=18, max=80, step=1),"street":fake.street_address(),"city":fake.city(),"state":fake.state(),"zip":fake.zipcode(),"lng":float(fake.longitude()),"lat":float(fake.latitude())}
    allData["records"].append(data)

json.dump(allData, output)