# method - function jo class ke andar define kiya jata hai use method kehte hai.


# 1, instance method  : aise method hote hai jo class ke object ke through call kiye jate hai aur inka pehla parameter self hota hai jo current object ke memory location ko hold karta hai.
# 2, class method     : aise method hote hai jo class ke naam ke through call kiye jate hai aur inka pehla parameter cls hota hai. is method ko define karne ke liye @classmethod decorator ka use kiya jata hai.
# 3, static method    : 




   #    class method 
   # ==========================================================



# class Student:
#     grad ='10th'
#     def __init__(self,name,roll_no):
#         self.n=name
#         self.r=roll_no
#     @classmethod                   #-------|
#     def update(cls,new):           #       |-------update class method
#         cls.grad=new               #-------|
# obj=Student('rahul',101)
# print(Student.grad)

# obj.update('12th')
# print(Student.grad)








# class Student:
#     grad ='10th'
#     def __init__(self,name,roll_no):
#         self.n=name
#         self.r=roll_no
#     @classmethod
#     def update(cls,new):
#         cls.grad=new
#     @classmethod
#     def add_new(cls,add):
#         cls.code=add
# obj=Student('rahul',101)
# obj.add_new(123)
# print(Student.code)






# static method  -  ek aise method jiska class method ya instance method se koi realition na ho
#================================================================================================


# class Student:
#     def __init__(self,roll):
#         self.n=roll
#     @staticmethod
#     def greet(name):
#         print(f'welcome {name} to my web page')
# obj=Student('rahul')
# x=obj.n
# obj.greet(x)
        