def make_func_repeater(f,x):
    def repeater(k):
        if k == x:
            return f(x)
        else:
            return repeater(k+1)
    return repeater(x)


