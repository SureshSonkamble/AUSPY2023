print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
ch=int(input("Enter your choice"))
n1=int(input("Entre number 1"))
n2=int(input("Entre number 2"))
if (ch==1):
    ans=n1+n2
    print("Sum:=",ans)      
if (ch==2):
    ans=n1-n2
    print("Sub:=",ans)     
if (ch==3):
    ans=n1*n2
    print("Mul:=",ans)            
    
