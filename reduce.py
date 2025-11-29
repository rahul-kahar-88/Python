
# reduce()
# ================================================================================


# syntex 
# ---------------------------------

# iterable
# def fun_name(parameter1,parameter2):
#     |
#     |
#     |
# res=reduce(fun_name,iterable,initial value)           # --------  (initial value) -- optional hai 
# print(res)




# que ---------------------------------


# import functools
# l=[1,2,3,4,5]
# def sum(x,y):
#     return x+y
# res=functools.reduce(sum,l)
# print(res)




# import functools
# l=[1,2,3,4,5]
# def sum(x,y):
#     return x*y
# res=functools.reduce(sum,l)
# print(res)




# from functools import reduce
# l=[11,20,38,40,54]
# def max(x,y):
#     if x>y:
#       return x
#     else:
#        return y
# res=reduce(max,l)
# print(res)





# from functools import reduce
# l=[1,2,3,4,5]
# def square(x,y):
#     return x+y**2   
# res=reduce(square,l,0)      # initial required
# print(res)





# from functools import reduce
# l=[1,2,3,4,5]
# def ft(x,y):
#     fact=1
#     for i in range(1,y+1):
#         fact=fact*i
#         return x+fact 
# res=reduce(ft,l,0)     
# print(res)