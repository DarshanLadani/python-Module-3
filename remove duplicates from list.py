l=input("Enter Values : ")
l=l.split()
print(l)
a=[]

for i in l:
    if i in a:
        l.remove(i)
    else:
        a.append(i)
print(a)
    
