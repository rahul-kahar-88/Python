
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







while(True):
    print("1.Add\n 2.Sub\n 3.Div\n 4.Mul\n 5.Exit")
    n=int(input("enter any number"))
    if n in (1,2,3,4,5):
        if n in (1,2,3,4):
            if n==1:
             number=int(input("how many number you want to add"))
             l=[]
             for i in range(1,number+1):
                value=int(input(f'enter{i} number'))
                l.append(value)
            sum=0
            for i in l:
             sum=sum+i
             print(f'addition {l} is {sum}')


            
        else:
           break
    else:
        print("please enter valid choice")