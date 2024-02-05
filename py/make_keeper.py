def make_keeper(n):
    def f(cond):
        i=1
        while i<n:
            if cond(i):
                print(i)
            i+=1
    return f

def is_even(n):
    return n%2==0

make_keeper(5)(is_even)