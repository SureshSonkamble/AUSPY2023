tpl=(1,2,'a',2.2,5,2,4,5)
print(tpl)
print(tpl[-1])
print(tpl[2])
print(tpl[4:7])
#access all value from tpl
cnt=0
for i in tpl:
    if(i==5):
        cnt=cnt+1

print(cnt)

