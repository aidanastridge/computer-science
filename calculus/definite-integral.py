
# functions

def one(x):
    return (1/2)*(x-1)**2

def two(x):
    return (1/2)*(x-1)**2

# integral

def integral(func,a,b):
    a = func(a)
    b = func(b)
    return b-a

print(integral(one,1,2))

