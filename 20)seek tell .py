f = open("text file 20.txt")

print(f.tell())# tells where the file pointer is in file
print(f.readline())
print(f.tell())

print(f.readline())
print(f.tell())

f.seek(10)# set pointer to specific position
print(f.tell())
print(f.readline())

f.close()
