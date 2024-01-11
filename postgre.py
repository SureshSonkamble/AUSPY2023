import psycopg2
from typing import Union
from fastapi import FastAPI
import json
app = FastAPI()
#establishing the connection
conn = psycopg2.connect(
   database="kthmres", user='postgres', password='Suresh@2023', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Executing an MYSQL function using the execute() method
cursor.execute("select * from users")
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
# Fetch all row using fetchall() method.
data = cursor.fetchall()
#print("Connection established to: ",data)
lst=[]
for i in data:
    print(i)
    lst.append(i)
#print(lst)
l=len(lst)
nm=[]
for d in range(l):
    #print(lst[d])
    for i in lst[d]:
        #print(i)
        nm.append(i)
print(nm[1::3])
print(nm[2::3])
print(nm[::3])
data=''
@app.get("/")
def read_root():
    return {'data':data}
#Closing the connection
conn.close()

