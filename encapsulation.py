

# access specifier/modifier
    #  1, public  --  variable/method(x,add()) ---  jo class ke ander aur class ke bahar kahi per bhi access ker sakte hai 
    #  2, protected  -- variable/method(_x,_add())  --- not supported 
    #  3, private   --  variable/method(__x,__add())  --- jo sirf apni hi class ke ander accessable ho aur kahi nhi 




# public - variable & method
# -------------------------------



# class A:
#     x=10
#     def show(self):
#         print("from class A")
#         print(A.x)
# class B(A):
#     pass
# obj=B()
# print(obj.x)
# obj.show()
# print(A.x)
# A.show(10)




# portected - variable & method
# --------------------------------------



# class A:
#     _x=10
#     def _show(self):
#         print("from class A")                   # python not supported
#         print(A._x)
# class B(A):
#     pass
# obj=B()
# print(obj._x)
# obj._show()
# print(A._x)
# A._show(10)



# private - variable & method
# ------------------------------------



class A:
    __x=10
    def __show(self):
        print("from class A")
        print(A.__x)         # inside class
class B(A):
    pass
obj=B()
# print(obj.__x)       #-----|----- through child class
# obj.__show()         #-----|
# print(A.__x)         #-----|----- outside class
# A.__show(10)         #-----|

print(dir(A))          # --->   _A__show' ,  '_A__x'
print(A._A__x)


# name mangal syntex --  __class_name__variable/method
# original name ko change kerke dusre name ko memory me save kerta hai

