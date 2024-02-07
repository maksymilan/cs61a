def haistone(n):
    if n==1:
        print(n)
        return 1
    elif n%2==0:
        print(n)
        return 1+haistone(n//2)
    else:
        print(n)
        return 1+haistone(n*3+1)

res = haistone(10)
print(res)