import json
f=open('test.json')
data=json.load(f)
#print(data)
print(data['posts']['status'])

for i  in range(11):
    print(data['posts']['post'][i]['CNAME'])
    

