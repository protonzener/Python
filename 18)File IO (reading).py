# file io basics
"""

"r" - open file for reading - default mode
"w" - open a file for writing 
"x" - creates file if not exists
"a" - add more content to a file 
"t" - text mode  - default mode
"b" - binary mode
"+" - read and write 
"""
# read mode is default (rt)
f = open("code.txt")



# to print line by line
# print(f.readline())
# print(f.readline())
# print(f.readline())




# to readlines in list 
print(f.readlines())









#--> to store in variable

# content = f.read()
# print(content)


"""content = f.read(3432)
print(content)"""











# for line in content:
#     print(line,end=" ")







# for line in f:
#     print(line,end=" ")


f.close



