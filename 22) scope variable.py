# l = 10 # this is global variable and can access to whole program 
# def func1(n):
#     #l =5 #local variable only limits to function
#     m = 43
#     global l #global l can change the value of global varible from function 
#     l =l + 23
#     print(l)
#     print(m)
#     print(n,"only prints the input")


# print(func1("func1 "))
# print(l)








# nested functions
x = 112
def he():
    x = 10
    def shel():
        global x
        x =1324
    print("before calling shel ",x)
    shel()
    print("after calling shel  ",x)

he()
print(x)