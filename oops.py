

#  OOPS = Object-Oriented Programming System 



# class Class_Name:
#     '''doc string'''
    # variables (properties) - 1, instance variable  2, class variable 3, local variable             ----|
    #                                                                                                    |---> 4 pillars of OOPS   
    # methods (behaviour) -  1, constructor 2, instance method 3, class method 4, static method      ----|




# class Student:
#     '''this is demo class'''
#     x=10
#     y=20
#     def show():
#         print("hello")
#     pass
# # print(dir(student))          # it will give all the default properties and methods of class student
# # print(Student.__doc__)       # it will give doc string of class student
# print(Student.__dict__)      # it will give all the properties and methods of class student in dictionary format





#  __init__  # constructor




# class Student:
#     '''this is demo class'''
#     x=10
#     y=20
#     def display():
#         print("hello")
# # print(dir(Student))          
# print(id(Student))
# obj = Student        # creating object of class student
# print(id(obj))        # both id will be same because both are pointing to same memory location
# obj2 = Student
# obj3 = Student  
# print(id(obj2), id(obj3))   # all three objects are pointing to same memory location of class student

# obj4 = Student()
# print(id(obj4))            # this object is created with () so it will have different memory location






# class Student:
#     def __init__(self):   #  reference parameters hai jo current class ke object ke memory location ko hold karte hai
#         print(" constructor called")
#         print(id(self))   # it will give the memory location of the object created
# obj1 = Student      
# print(id(obj1),id(Student))
# obj2 = Student()     # creating object of class student with () so it will call constructor
# print(id(obj2),id(Student))            # this object is created with () so it will have different memory location   







# class Student:
#     x=10
#     y=20
# obj=Student                   # (internal constructor)
# obj1=Student()                # (external constructor)
# print(id(obj),id(obj1))




# class Student:
#     school = 'SHSS'
#     school_city = 'bhopal'
#     def detail():
#         print("from student class")
# obj = Student
# print(obj.school,Student.school)
# print(obj.school_city,Student.school_city)
# obj.detail()
# Student.detail()





# class Student:
#     school = 'SHSS'
#     school_city = 'bhopal'
#     def detail(self):                                 # recommandation hai pahala parameter self hoga ----  ye instance method hota hai 
#         print("from student class")
# obj = Student()
# print(obj.school,Student.school)
# print(obj.school_city,Student.school_city)
# obj.detail()






# class Student:
#     def __init__(self,name,age,grad):
#         self.n=name
#         self.a=age
#         self.g=grad
#     def display(self):
#         print(self.n,self.a,self.g)         #----|
# obj=Student('rahul',20,'BCA')                   #|---- this is internal print
# obj.display()                               #----|
# # print(obj.n,obj.a,obj.g)                     # ----|--- this is for external print
# Student('tanmay',23,'b-tech').display()        # ----|