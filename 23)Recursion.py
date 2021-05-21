# recursive and iterative approach

# 5 * fac_recursive(4)
#  5 * 4 *fac_recursive(3)
# .
# .
# .

def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
    
    """ 
    :param n: integer
    :return :n*n-1*n-2 ....__annotations__
    """

def fac_recursive(n):
    if n==1:
        return 1
    else:
        return n * fac_recursive(n-1)

number = int(input("Enter the number : "))
print("Factorial using iterative is ",factorial(number))
print("Factorial using recursive is ",fac_recursive(number))


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(number))