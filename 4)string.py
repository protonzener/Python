mystr = "I am proton"
print(mystr)
print(mystr[0:7]) #string slicing
print(mystr[::])
print("\n")

#lenght
print(len(mystr))
print(mystr[0:11:2]) # skipping character by 2

print("\n")
print(mystr[-1::-1])#reversing the string
print(mystr[::-1])
print(mystr[::-2])
print("\n")

print(type(mystr))
print(mystr.isalnum())#alfa numberic (consisting of or using both letters and numerals)
print(mystr.isalpha())
print("\n")

print(mystr.endswith("proton"))#last word check
print(mystr.count("o"))#for counting character
print("\n")

print(mystr.capitalize())#makes first word capital
print(mystr.lower())#makes all lower
print(mystr.upper())
print("\n")

print(mystr.find("am")) # to find position of character
print(mystr.replace("am","are"))


