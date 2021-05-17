#for loops
list1 =[[1,2,3],'safe',5,33,43,324,'car','hello','proton']

for item in list1:
    print(item)
print("\n")

list2 = [['hello',1],['world',2]]
for item,value in list2:
    print(item,value)

print("\n")

dict1 = dict(list2)
for item in dict1.items():
    print(item)

print("\n")
for i in list1:
    if str(i).isnumeric() and i>3:
        print(i)

print("\n")
for i in range(10):
    print(i)