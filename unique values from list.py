l=input("Enter Values : ")
l=l.split()
print(l)
a=[]

for i in l:
    if i not in a:
        a.append(i)
    
print(a)
    
