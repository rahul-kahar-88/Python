# variable 
    #    1, instance variable    |
    # =========================== 
  
#  declaration : 
#           1, in-side class - 
#             a, in-side constructor
#             b, in-side instance method
#           2, outside class


# calling :
#           1, inside class -
#             a, inside constructor 
#             b, inside instance method
#           2, outside class



#  instance variable = jo variable class ke andar aur constructor ya instance method ke andar declare kiya jata hai aur                                                          jiska scope pura object hota hai use instance variable kehte hai.




# class Student:
#     def __init__(self, name, contact):    #  reference parameters hai jo current class ke object ke memory location ko hold karte hai
#         self.n = name                     # declaring inside constructor
#         self.c = contact                  # declaring inside constructor
#         print(self.n,self.c)              # calling inside constructor
#     def add_new(self,roll_no):            # instance method
#         self.r = roll_no                  # declaring inside instance method
#     def display(self):
#         print(self.n,self.c,self.r)       # calling inside instance method
# obj = Student("rahul",1234567890)         # creating object of class student with () so it will call constructor
# obj.add_new(101)                          # calling instance method 
# obj.display()
# obj.email = 'rahulkahar@gmail.com'        # declaring outside class
# obj.display()                             # calling instance method 
# print(obj.n,obj.c,obj.r,obj.email)        # calling  outside class 




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2, class variable         |
# ===========================


# decloration :
          # 1, inside class - a, inside constructor
          #                   b, inside instance method
          #                   c, inside class method
          # 2, outside class

# calling :
          # 1, inside class - a, inside constructor
          #                   b, inside instance method
          #                   c, inside class method
          # 2, outside class



# class variable = jo variable class ke andar aur constructor, instance method ya class method ke andar declare kiya jata hai aur jiska scope pura class hota hai use class variable kehte hai.



# note : class depended variable ko hum class variable kehte hai.



# class Student:
#     School_name = "ABC School"          # declaring inside class
#     def __init__(self, name, roll_number):   
#         self.n = name                      # declaring inside constructor
#         self.r = roll_number               # declaring inside constructor
#         Student.School_city = "bhopal"    # declaring inside constructor 
#         print(Student.School_name,Student.School_city)   # calling inside constructor 
#     def add_new(self): 
#         Student.School_code = 101   # declaring inside instance method
#         print(Student.School_name,Student.School_city,Student.School_code,Student.contact)  # calling inside instance method
# Student.contact = 1234567890   # declaring outside class
# obj = Student("rahul",101)    # creating object of class student with () so it will call constructor
# obj.add_new()                 # calling instance method 
# print(Student.School_name,Student.School_city,Student.School_code,Student.contact)  # calling outside class  - class variable ko hum class ke naam se hi access karte hai na ki object ke naam se.




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3, local variable        |
# ===========================
 
# definition : jo variable kisi function ya method ke andar declare kiya jata hai aur jiska scope sirf usi function ya method tak hota hai use local variable kehte hai.



# class Student:
#     def __init__(self):
#         x=10               # local variable
#         print(x)          # calling local variable inside constructor
#     def new(self):
#         y=20               # local variable
#         z=y+10
#         print(z)          # calling local variable inside instance method
#       #  print(x)         #  - error because x ka scope sirf constructor tak hi hai
# obj=Student()            # creating object of class student with () so it will call constructor
# obj.new()                # calling instance method





# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
