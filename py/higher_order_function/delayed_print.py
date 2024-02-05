"""def delayed_print(x):
    old = x
    def pre(y):
        nonlocal old
        old_cp = old
        old = y
        return old_cp
    return pre

delayed_print(1)(2)"""
def delayed_print(x):
    pre_arg=x
    def print_delay(y):
        nonlocal pre_arg
        pre_arg_cp=pre_arg
        pre_arg=y
        print(pre_arg_cp)
        return pre_arg_cp
    return print_delay

f = delayed_print(1)#返回的函数不执行
f = f(2)    
f = f()
f = f(2)