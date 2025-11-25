

# ==================== variable scope ========================

# 1, -- local
# 2, -- global
# 3, -- nonlocal




# 1, local :-  access within the block
# ---------------------------------------------

# def display():
#     x=10           # local variable
#     print(x)
# display()
# print(x)           # NameError: name 'x' is not defined



# 2, global :- through out pure code me accessable ho
# -----------------------------------------------------


# def display():
#     global x
#     x=10           
#     print(x)
# display()
# print(x)




# def display():
#     global x
#     x=10              # --- -- error aata hai isme 
#     print(x)
# print(x)  
# display()
# print(x)




# x=10
# def show():
#     print(x)
# print(x)
# show()
# print(x)




# x=10
# def show():
#     x=20
#     print(x)
# print(x)
# show()
# print(x)




# x=10
# def show():
#     print(x)      #LocalError: cannot access local variable 'x' where it is not associated with a value
#     x=20
#     print(x)
# print(x)
# show()
# print(x)




# x=10
# def show():
#     x=20
#     print(globals()['x'])         # (globals()['x']) ---- [Method] for using global value in local
# show()




# 3, nonlocal :- 
# --------------------------------------------------------------------



def show():
    x=10
    def display():
        nonlocal x
        x=x+5
        print(x)
    display()
show()
