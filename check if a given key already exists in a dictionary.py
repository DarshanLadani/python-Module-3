d={1:4, 2:8, 3:92, 4:82, 5:'python', 6:'java', 7:'tops', 8:8.8}
print(d)
try:
    a=int(input("Enter Key : "))
    if a in d.keys():
        print("Key is alredy exists")
    else :
        print("Key is not exists")
except Exception as d:
    print("Exception caught : ",d)
finally :
    print("\n")
