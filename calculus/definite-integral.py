
# functions

def one(x):
    return (1/2)*(x-1)**2

def two(x):
    return 5*x

# integral

def integral(func,a,b,c,e):
    a = (c*func(a))**e
    b = (c*func(b))**e
    return b-a


print(integral(one,1,2,1,1))

# 4 

print(integral(two,1,2,5,1))
print(integral(two,-2,2,1,1))
print(integral(two,1,1,1,2))
print(integral(two,2,-2,4,1))

# 5

