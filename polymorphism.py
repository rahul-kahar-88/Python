
# ek hi function ke kai output deta hai to ise polymorphism kehte hai

 

# method polymorphism
# -----------------------


class A:
    def sound(self):
        print("from A")
class B:
    def sound(self):
        print("from B")
l=[A(),B()]
for i in l:
    i.sound()
        






