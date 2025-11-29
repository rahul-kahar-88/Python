

# map()   -  args me function pass kerte hai
# =================================================================

# syntex -----------

    #   iterable3
    #   iterable2
    #   iterable1
      
    #   def fun_name(parameter1,parameter2,parameter3):
    #      |
    #      |
    #      |
    #   res=map(fun_name,iterable1,iterable2,iterable3)
    #   print(res)
    #   print(list(res))


# -----------------------------------------------------------------------

# example :-



# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[3,2,4,1]
# def add(x,y,z):
#     return x+y+z
# res=map(add,l1,l2,l3)
# print(res)
# print(list(res))


           


# l1=[1,2,3,4,5]
# l2=[5,6,7,8]
# l3=[3,2,4]            # total number of input = total number of output
# def add(x,y,z):
#     return x+y+z
# res=map(add,l1,l2,l3)
# print(res)
# print(list(res))
        




# l1=[1,2,3,4]
# def square(n):
#     return n**2
# res=map(square,l1,)
# print(res)
# print(list(res))






l1=[1,2,3,4]
def sqrt(n):                 # square root
    return n**0.5
res=map(sqrt,l1,)
print(res)
print(list(res))