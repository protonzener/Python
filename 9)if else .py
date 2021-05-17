var1 = 6
var2 = 34

list = [1, 2, 3, 4, 5]
if 5 not in list:
    print("True")
else:
    print("False")

print("Enter var3:")
var3 = int(input())
if var3 > var2:
    print(f"{var3} is Greater than {var2}")
elif var2 == var3:
    print(f"{var3} is equal to {var2}")
else:
    print(f"{var3} is smaller than {var2}")
