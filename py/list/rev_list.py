def rev_list_1(s):
    def rev_list_helper(s,rev_sub_s = ''):
        if len(s) == 1:
            return s + rev_sub_s
        else:
            return rev_list_helper(s[1:],s[0] + rev_sub_s)
    return rev_list_helper(s)

def rev_list_2(s):
    if len(s) == 1:
        return s
    else:
        return rev_list_2(s[1:]) + s[0]

print(rev_list_1("12345"))
print(rev_list_2("12345"))