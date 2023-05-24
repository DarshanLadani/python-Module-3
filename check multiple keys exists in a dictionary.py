d={1:4,2:8,3:2,4:15,5:36,6:99,7:88,8:89,9:20}
print(d.keys())
c=False
for i in d.keys():   
    for j in d.keys():
        print(i," IIIIIIIIII ")
        print(j," J ")
        if i==j:
            c=True

print(c)
