l=input("Enter List 1 : ")
l1=input("Enter List 2 : ")
l=l.split()
l1=l1.split()
print(l)
print(l1)
result=False
for i in l:
    for j in l1:
        if i==j:
            
             result = True
print(result)
