def print_n(n):
    def inner_print(x):
        nonlocal n
        if n==0:
            print("done")
        else:
            print(x)
            n-=1
        return None
    return inner_print

f=print_n(3)
f("hello")
f("hi")
f("yo")
f("wow")