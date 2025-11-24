

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
# 6, variable length key word args



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


# ======================= 4, key word args ==========================


# def ref (x,y,z):
#     print(z)
#     print(x)
#     print(y)
#     # print(x,y,z)
# p=10
# q=20
# r=30
# ref (z=p,y=q,x=r)



# def ref (x=0,y=0,z=0):
#     print(z)
#     print(x)
#     print(y)                              # isse error nhi aayega
#     # print(x,y,z)
# p=10
# q=20
# r=30
# # ref (z=p,y=q,x=r) 
# # ref (z=p) 
# ref (z=p,y=q) 




# =========================== 6, variable length key word args =================================


# def fun_name(**kwargs):   #---- packing
#     print(kwargs)
#     print(type(kwargs))
# # fun_name(x=10,y=20,z=30,p=2,q=5)
# fun_name(**eval(input("enter any dict : ")))    #  ------------ unpacking





# def fun_name(**kwargs):

#     # for i in kwargs.keys():
#     #     print(i)

#     # for i in kwargs.values():
#     #     print(i)

#     for i,j in kwargs.items():
#         print('key =' , i , 'value = ',j)

# fun_name(x=10,y=20,z=30)





# ================================= summary ================================================

# def fun_name(x,y=0,*z,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# fun_name(10,20,30,40,50,p=5,r=2,s=1,t=3)




# def fun_name(x,*z,y=0,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# fun_name(10,20,30,40,50,p=5,r=2,s=1,t=3)




# def fun_name(x,p,*z,y=0,**q):
#     print(x)
#     print(y)                                              # --- -- error aata hai isme 
#     print(z)
#     print(p)
#     print(q)
# fun_name(10,p=5,20,30,40,50,r=2,s=1,t=3)










# def natural_number(n):
#     for i in range(1,n+1):
#         print(i)
# n=int(input("enter any value : "))
# natural_number(n)




# def natural_number(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
# n=int(input("enter any value : "))
# natural_number(n)




def natural_number(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
        print("prime number")
        pass
    else:
        print("not a prime ")
        pass
n=int(input("enter any value : "))
natural_number(n)