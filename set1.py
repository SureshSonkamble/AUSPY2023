st={'a','b','c','d','z','z','z'}
print(st)
s=input("Enter value to be search")
print(s in st)
t=0
f=0
for i in st:
    #print(s)
    if(i==s):
        #print("value found")
        #break
        t=1
    else:
        #print("Value not found")
        #break
        f=1
if(t==1):
    print("value found")
else:
    print("value not found")




    
        
