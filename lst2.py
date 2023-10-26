lst=[1,2,3,4,5,6,7,2,3,2,4,2,2,4]
print(lst)
cnt=0
n=int(input("Enter number to be search"))
for i in lst:
    #print(i)
    if(i==n):
        cnt=cnt+1
print(n,"accurance ",cnt,'Times')
