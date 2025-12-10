#  parent   <-----  child



# class Parent:
#     x=10
#     def home(self):
#         print("from parent class")
# class child(Parent):
#     pass
# obj=child()
# print(obj.x)
# obj.home()


# Type :-
        #   1, Single-level :     parent  ----->  child
        #   2, Multi-level :      Grand parent -----> parent -----> child
        #   3, multiple :         parent 1        parent 2
        #                            |               |
        #                            |               |
        #                             \--- child ---/
        #
        #  4, Hierarichical :     parent 
                            #    ___/\___
                            #   /        \
                        #    child1    child2

        #   5, hybrid             parent 
                            #    ___/\___
                            #   /        \
                        #    child1    child2
                            #   \          /
                             #   \        /
                                # sub-child



# Single-level Inheritance
# ---------------------------------------------------

# class parent:
#     x=10
#     def home(self):
#         print("home from parent")
# class child(parent):
#     def home(self):
#         print("home from child")
#         super().home()               #  --------  super method ki madad se parent ke home ko call karege
# obj=child()
# obj.home()
      



# Multi-level Inheritance
# ------------------------------------------------------


# class grandparent:
#     def home(self):
#         print("home from grandparent")
# class parent(grandparent):
#     def home(self):
#         print("home from parent")
#         super().home()
# class child(parent):
#     def home(self):
#         print("home from child")
#         super().home()
# obj=child()
# obj.home()



# Multiple Inheritance
# ----------------------------------------------------------


# class father:
#     def home(self):
#         print(" home from father")
#         mother().home()
#         # mother.home(self)               #  ------ optional hai 
# class mother:
#     def home(self):
#         print("home from mother")
# class child(father,mother):             # mro - method resolution order
#     def home(self):
#         print("home from child")
#         super().home()
# obj=child()
# obj.home()



# hierarichical inheritance
# ---------------------------------------------------------------------

# class A:
#     def home(self):
#         print("home from A")
#         B().home()
# class B(A):
#     def home(self):
#         print("home from B")
# class C(A):
#     def home(self):
#         print("home from C")
#         super().home()
# obj=C()
# obj.home()






# hybrid inheritance
# -------------------------------------------------------------------------

# class A:
#     def home(self):
#         print("home from A")
        
# class B(A):
#     def home(self):
#         print("home from B")
#         super().home()
# class C(A):
#     def home(self):
#         print("home from C")
#         A().home()
# class D(B,C):
#     pass
# obj=D()
# obj.home()