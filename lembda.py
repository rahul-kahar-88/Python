# lembda function  - aisa function jiska name nhi hota python me usko lembda function kahte hai
# =========================================


# x = lambda x,y,z:2*x+y+z
# print(x(1,2,3))




# x = lambda x,y :  x if y<x else y
# print(x(5,10))




# Syntax  ---- 

# lambda x,y : if_result if condition else else_result





# x = lambda age: 'child' if 0<age<18 else ('adult' if 17<age<60 else ( 'senior' if 59<age else 'invald age'))
# age = int(input("enter your age "))
# print(x(age))




# x = lambda n:'even' if n%2==0 else None
# n=int(input("enter number : "))
# print(x(n))





# x = lambda n:n**2
# n=int(input("enter number : "))
# print(x(n))





# x = lambda p,q:p+q
# print(x(5,10))




# n=10
# x=lambda n:[i for i in range (1,n+1) ]
# print(x(n))




# n=10
# x=lambda n: [i for i in range (1,n+1)if i%2==0]
# print(x(n))




# l=[1,2,3,4,5]
# print(list(map(lambda n: n**2,l)))




# l1=[1,2,3,4]
# l2=[2,5,4,5]
# l3=[6,7,8,9]
# print(list(map(lambda x,y,z: x+y+z,l1,l2,l3)))




# l1=[1,2,3,4]
# l2=[2,5,4,5]
# l3=[6,7,8,9]
# print(list(map(lambda x,y,z: x-y-z,l1,l2,l3)))




# l1=[1,2,3,4]
# l2=[2,5,4,5]
# l3=[6,7,8,9]
# print(list(map(lambda x,y,z: x*0.5+y*0.5+z*0.5,l1,l2,l3)))





# x=[1,2,3,4,5,6,7]
# print(list(filter(lambda x: 'even' if x%2==0 else None,x)))



from functools import reduce
x=[1,2,3,4,5,6,7]
print(reduce(lambda x,y: x+y ,x ))