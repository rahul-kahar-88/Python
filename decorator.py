
# decorator -----  internal code ko bina change kiye hua uska internal Behavior change kr deta hai
# ========================================================================================================


# represented by - @ symbol



# def decore( ):
#     def inner():
#         print("hey")
#     return inner
# x=decore()
# print(x)
# x()




# def decore( fun):
#     def inner():
#         fun()
#     return inner
# def add():
#     print("hey")
# res=decore(add)
# res()






# def decore( fun):
#     def inner(p,q):
#         p=p+5
#         q=q*2
#         fun(p,q)
#     return inner
# def add(x,y):
#     print(x+y)
# res=decore(add)
# res(10,20)





# def decore( fun):
#     def inner(p,q):
#         p=p+5
#         q=q*2
#         fun(p,q)
#     return inner
# @decore
# def add(x,y):
#     print(x+y)
# add(10,20)





# def first( fun):
#     def inner():
#         print("welcome")
#     return inner
# @first
# def great():
#     print("hey")
# great()






def decore(fun):
    def inner(x):
        for i in range (1,x+1):
            print(2*i-1)
    return inner
@decore
def even(n):
    for i in range (1,n+1):
        print(2*i)
n=int(input("enter n value :- "))
even(n)





# ========================================================================================================