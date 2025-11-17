
# ================================ while loop ==================================


#syntax
# initialization
# while condition
#       while-body executed
#       when condition is true
#------------------------------------------------------
#1. initialize starting point 
#   while (terminating point)      ---------------->infinite
#       while-body
#--------------------------------------------------------
#2. initialize starting point 
#   while (terminating point)      ---------------->finite
#      while-body
#      Increment/decrement






# n = int(input("enter any number : ")) 
# td = 0
# while n > 0:
#     td = td + 1
#     n = n//10
# print("total digit : ", td)






# n = int(input("enter any number : ")) 
# m =n             #  |--- [m=p=n]
# p=n              #  |
# td = 0
# sum = 0
# while n > 0:
#     td = td + 1
#     n = n//10
# while m > 0:
#     ld = m%10 
#     sum=sum+ld**td
#     m = m // 10
# if p==sum:
#     print(f'given number {p} is armstrong')
# else:
#     print(f'given number {p} is not armstrong')