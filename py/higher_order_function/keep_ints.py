def keep_ints(cond,n):
    i=1
    while i<n:
        if cond(i):
            print(i)
        i+=1

def is_even(n):
    return n%2==0

keep_ints(is_even,5)
