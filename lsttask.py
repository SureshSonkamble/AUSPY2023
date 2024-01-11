lst=((1, 'Jerry', 'jerry@example.com'),
(3, 'suresh', 'suresh@gmail.com'),
(7, 'test', 'aaa'),
(4, 'testing', 'updatetest'),
(11, 'insert', 'inserttest'),
(8, 'insert', 'inserttest'))
print(lst)
p=0
n=[]
for i in lst:
    p=(i[1::3])
    for j in p:
        n.append(j)

print(n)
        


