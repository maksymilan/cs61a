def make_adder(n):
    def adder(k):
        return n+k
    return adder
adder_3 = make_adder(3)
res = adder_3(5)
##when you want to define a function that its return value is a function,
## you define the returned function in the body of the main function
##and the return must be the name of the function,such as adder_3 instead of adder_3(x),the latter is a number and x is not defined,it has syntax error
adder_4 = lambda x:x+4
print(adder_4(5))
##Newton's method
def average(x,y):
    return (x+y)/2
def aprox_eq(x,y,tolerance=1e-4):
    return abs(x-y)<tolerance
def improve(update,close,guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def s_qrt(a):
    def sqrt_update(x):
        return average(x , a/x)
    def sqrt_close(x):
        return aprox_eq(x*x,a)
    return improve(sqrt_update,sqrt_close)
print(s_qrt(2))