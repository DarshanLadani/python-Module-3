d={1:4, 2:8, 3: 2, 4:15}
print(d)
print(d.values())
for i in d.values():
    for j in d.values():
        if j>i:
            temp=i
            i=j
            j=temp
b=list(d.values()).sort()
print(b)
