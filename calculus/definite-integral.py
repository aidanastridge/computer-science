
# integral
def integral(func,a,b,c,e):
    a = (c*func(a))**e
    b = (c*func(b))**e
    return b-a

#Quick check
# 3
def three(x):
    return (1/4)*(2*x-8)**2


# 4 
def four(x):
    return 5*x

#Excersises
# 17
def seventeen(x):
    if(x>=0):
        return abs(x-2)
    else:
        return x+2

# 18
def seventeen(x):
    if(x>=1):
        return x**2
    else:
        return 2*x


