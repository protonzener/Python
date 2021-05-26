# anonymous or lambda function

minus = lambda x,y: x-y
print(minus(96,45))

def a_first(a):
    return a[1]

a = [[1,44],[5,9],[6,7]]
a.sort(key=a_first)
print(a)