s="abdcbabbabajss"
ch=input("Enter charactre to be search")
cnt=0
for i in s:
    if(i==ch):
        cnt=cnt+1

print(ch,"found ",cnt, "Number of time")
