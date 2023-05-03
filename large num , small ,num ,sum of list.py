l=[1,34,23,3.3,65,90,99,0.8,12]
temp=0
print(l)
l.sort()
print(l)
print("Smallst Number : ",l[0])
print("Largest Number : ",l[-1])
for i in l:
    temp+=i
print("Sum of List : ",temp)
