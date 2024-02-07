def is_prime(n):
    def is_prime_helper(k,n):
        if n == 1:
            return False
        if k > n/2:
            return True
        else:
            if n%k == 0:
                return False
            else:
                return is_prime_helper(k+1,n)
    return is_prime_helper(2,n)