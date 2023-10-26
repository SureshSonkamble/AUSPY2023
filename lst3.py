lst=[]
n=int(input("Enter the number you want to add"))
for i in range(n):
    val=input("Enter value for list")
    lst.append(val) #add value into list
print(lst)

dl=input("Enter value for list you want to remove")
lst.remove(dl) #delete value form list
print(lst)

up=input("Enter value for list you want to update")
i=int(input("Enter index for list you want to update"))
lst[i]=up
print(lst)
