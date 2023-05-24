l=[(1,2,3,4),(),(23,56,8,9),(),(5,8,9,6,4),()]
for t in l:
    if t==():
        l.remove(t)
print(l)
