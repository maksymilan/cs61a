def recursive_sum(n):
    if len(range(n)) == 0:
        return 0
    else:
        return list(range(n))[len(list(range(n)))-1] + recursive_sum(n-1)
print(recursive_sum(5))