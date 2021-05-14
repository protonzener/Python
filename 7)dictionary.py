dict ={'volvo':'safe cars',
'proton':'+ve',
'electron':'-Ve'}
print(dict)
print("\n")

#to access keys
print(dict['proton'])

#to add key and value
dict[420]='kahli'
print(dict)
print("\n")

#to delete
del dict[420]
print(dict)
print("\n")

d3 =dict.copy()
print(d3)

#to get value
print(dict.get("proton"))

#to update 
dict.update({"proton":"value"})
print(dict)



#user i/p
dict ={'volvo':'safe cars',
'proton':'+ve',
'electron':'-Ve'}

word =input("Enter the word to get meaning:")
print(dict.get(word))