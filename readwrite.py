f=open("PYTEST.txt",'w')
data=input("Enter data to be write in file")
f.write(data)
f.close()
print("data writen sucess")
#file read
f=open("PYTEST.txt",'r')
#print(len(f.read()))
x=f.read()
print(x)
for i in x:
    print(i)
