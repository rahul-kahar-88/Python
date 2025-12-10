# abstraction ---
            # 1, abstract class
            # 2, abstract method
            # 3, concrete method



# abstract class 
# -----------------------------------------------

# ABC - abstract base class

# -  kam se kam ek inheritance class ho
# -  kam se kam ek abstract method ho
# -  kam se kam ek concrete method ho





from abc import ABC , abstractmethod
class A(ABC):
    def dashboard(self):
        print("welcome to dashboard")
    @abstractmethod
    def login(self):
        pass
class B(A):
    def login(self):
        print("login successfully")
obj=B()
obj.login()