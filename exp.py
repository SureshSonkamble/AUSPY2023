a=2
b='2'
print("Normal flow1")
try:
    ans=a+b
    print(ans)
except Exception as e:
    print("Error")
finally:
    print("Allaway execute")
    

