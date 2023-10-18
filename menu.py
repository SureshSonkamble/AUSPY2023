print("***************************************")
print("1.Square")
print("2.Cube")
print("3.Area")
print("4.even odd number")
print("***************************************")
ch=int(input("Enter your choice"))
if(ch==1):
    n=int(input("Enter your number"))
    print("Square of number is:=",n*n)
if(ch==2):
    n=int(input("Enter your number"))
    print("Cube of number is:=",n*n*n)
if(ch==3):
    r=int(input("Enter your radius"))
    print("Area of circle is:=",3.14*r*r)
if(ch==4):
    n=int(input("Enter your number"))
    if(n%2==0):
        print(n,"is Even number ")
    else:
         print(n,"is Odd number ")
if(ch>4):
    print("Invalid Choice plase enter choice between 1 to 4 only")



    
    
