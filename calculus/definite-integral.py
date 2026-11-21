
# functions

def three(x):
    return (1/4)*(2*x-8)**2

def four(x):
    return 5*x

# integral

def integral(func,a,b,c,e):
    a = (c*func(a))**e
    b = (c*func(b))**e
    return b-a


# quick check

# 3

print(integral(three,2,7,1,1))

# 4 

print(integral(four,1,2,5,1))
print(integral(four,-2,2,1,1))
print(integral(four,1,1,1,2))
print(integral(four,2,-2,4,1))

# 17

def seventeen(x):
    return x