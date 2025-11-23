

#   1 = In-build function ---
#   2 = user define function ---
#
#
# 

# =================  syntex of user defined ================
#
#
#                   required variable in function body
#                       ^
#                       |
#   def fun-name(parameter):
#        |
#        |  fun-body
#        |
#        |   return
#   fun-name(arguments)  --->   value again parameter








# def hey():
#     print("hey rahul")
# hey()




# def xyz():
#     pass
# xyz()





# def add (x,y):
#     print(x+y)
#     return None
# p=int(input("enter any number : "))
# q=int(input("enter any number : "))
# res=add(p,q)
# print(res)
# print(res)
# print(res)
# print(res)





# def add (x,y):
#     z=x+y
#     return z
# p=int(input("enter any number : "))
# q=int(input("enter any number : "))
# res=add(p,q)
# print(res)
# print(res)
# print(res)
# print(res)




# print(print("hey"))




# def add (x,y):
#     print(x+y)
# p=10
# q=20
# print(add(p,q))





# def add (x,y):
#     print(x+y)
#     return (x+y)
# p=10
# q=20
# print(add(p,q))





# user define function  ==================== 
#  with argument   -----  1, with return     2, without return
#  without argument  ----  1, with return     2, without return 

# function me return use kerna hi padega Python me 





# ===============================================================================================================================================================================


# relation between argument and parameter

# 1, positional argument
# 2, default positional arg
# 3, variable length positional arg
# 4, key-word arg
# 5, 



# * --- args   ------    for holing tuple
# ** ---   kwargs [key-word args]  ------ for dictionary




# ==================== 1, positional argument =====================================

# def add(x,y,z):
#     return x+y+z
# p,q,r=int(input("enter 1st number")),int(input("enter 2nd number")),int(input("enter 3rd number"))
# res=add(p,q,r)


# res=add()              ##TypeError: add() missing 3 required positional arguments: 'x', 'y', and 'z'
# res=add(p)             ##TypeError: add() missing 2 required positional arguments: 'y' and 'z'
# res=add(p,q)           ##TypeError: add() missing 1 required positional argument: 'z'
# res=add(p,q,r,5)       ##TypeError: add() takes 3 positional arguments but 4 were given

# print(res)



# ======================= 2, default positional args =================================


# def add(x=0,y=0,z=0):
#        return x+y+z
# res = add()        # o/p --- 0

# res = add(10)      # o/p --- 10
# res = add(10,20)      # o/p --- 30
# res = add(10,20,30)      # o/p --- 60
# res = add(10,20,30,40)      # TypeError: add() takes from 0 to 3 positional arguments but 4 were given

# print(res)



# ====================== 3, variable length positional args ============================


# def add(*args):           # recomanded  args
#     print(args)
#     print(type(args))
# add(1,2,3,4,5,6,7,8,9,10)





# def add (*n):
#     print(n)
#     print(type(n))
#     # sum=0
#     # for i in n:
#     #     for j in i:
#     #         sum=sum+j
#     # return sum
# x = add(*eval(input("enter any value : ")))
# print(x)