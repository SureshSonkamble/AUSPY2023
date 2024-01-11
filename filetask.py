#file read
f=open("india.txt",'r')
fl=f.read()
x=fl.split(" ")
e=[]
o=[]
for i in x:
    if(int(i)%2!=0):
        e.append(i)
       
        #print(e)
    else:
        o.append(i)
        '''f=open('even.txt','a')
        f.write(" "+i)
        f.close()'''
        #print(o)
print("Sucess")
print(e)
print(o)
for i in e:
     f=open('odd.txt','a')
     f.write(" "+i)
     f.close()
print("file writen success")

     
    



