# def outer(num):
#     def inner(num_in):
#         print('inner, num_in is %s'% num_in)
#         return num + num_in
#     return inner
# inner = outer(20)
# print(inner(20))


x = 2
def outer():
    x = 0
    def inner():
        global x
        print(x)
        m = x+1
        print(m)
    return inner
f = outer()
f()