pwd=input("Enter Your Password")
print(pwd)
l=len(pwd)
print(l)
#print(pwd.isupper())
#print(pwd.islower())
#print(pwd.isdigit())
lc=0
uc=0
d=0
for i in pwd:
    if(i.isupper()):
        uc=1
    if(i.islower()):
        lc=1
    if(i.isdigit()):
        d=1
#print(uc,lc,d)
if(uc==1 and lc==1 and d==1 and l>=8):
    print("Valid password")
else:
    print("Invalid password")

    

        
