""" Merges two numbers
>>> merge(31, 42)
4321
>>> merge(21, 0)
21
>>> merge (21, 31)
3211
"""
def merge(m,n):
    if m < 10 and n < 10:
        return max(m,n) * 10 + min(m,n)
    elif m == 0 or n == 0:
        return 0