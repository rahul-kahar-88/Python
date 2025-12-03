


# x = range(1,100)
# print(list(x))
# print(id(list(x)))




# def natural_no(n):
#     i=1
#     while i <=n:
#         yield i
#         i=i+1
# x = int(input("enter any number :- "))
# res= natural_no(x)
# print(res)
# for i in res:
#     print(i)

# print(next(res))
# print(next(res))
# print("hey")
# print(next(res))

# for _ in range(2):
#     print(next(res))

# for _ in range(10):
#      try:
#         print(next(res))
#      except StopIteration:
#          print("all element are iterated , i.e collection empty")
        #  break
     


# ================================================================================================
# iterable and iterator ---------------- list , tuple , string , dist



l = [1,2,3,4,5]            # -------- [iterable]
print(l)
x=iter(l)                  # -------- [iterator]
print(x)
# for i in  x :
#     print(i)
for i in range(6):
    print(next(x))
