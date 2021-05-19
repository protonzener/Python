f = open("text file 19.txt","a")#append mode
a =f.write("Hello world from vs code \n ")
print(a)
f.close()

# handle read and write mode
f = open("text file.txt","r+")#read and write mode
a =f.write("Hello world from vs code \n ")

f.close()


