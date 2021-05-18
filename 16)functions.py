# a = 3
# b =35
# c = sum((a,b))
# print(c)


def func1():
    print("You are in function 1", )


func1()
print("\n")


def func2(c, d):
    """This function gives average of two number"""
    average = (c + d) / 2
    # print(average)
    return average


v = func2(23, 34)
print(f"using variable =>", v)
print(f"using direct function calling =>", func2(23, 34))

print("\n")
print(func2.__doc__)

print('\n')


def my_function(x):
    """multiply x by 5 """
    return 5 * x


num = int(input("Enter the number to multiply it by 5 : "))

print(my_function(num))
