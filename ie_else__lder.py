s1=int(input("Enter sub1 marks"))
s2=int(input("Enter sub1 marks"))
s3=int(input("Enter sub1 marks"))
if(s1>100 or s2>100 or s3>100):
    print("Invalid marks")
else:    
    ttl=s1+s2+s3
    per=ttl/3
    print("Total:=",ttl)
    print("Per %:=",per)

if(per>=75):
    print("O grade")
elif(per<75 and per>=60):
    print("A grade")
elif(per<60 and per>=50):
    print("B grade")
elif(per<50 and per>=40):
    print("D grade")
else:print("FAIL...")

    


    


    
    

