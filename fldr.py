import os
try:
    for i in range(1,10):
        path='D:AUSPY\FLDR'+str(i)
        os.makedirs(path)
        f=open(path+'/'+'a.txt','w')
        f.write("Notice...")
        print("Success")
except Exception as e:
    print(e)
