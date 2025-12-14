
# cursor-movement --
# ----------------------

    # tell() - to check cursor current position
    # seek() - to move our cursor to required position




#       tell() -
# -------------------

# f=open('n4.txt','x+')
# print(f.tell())

# f=open('n4.txt','w+')     # 0
# print(f.tell())

# f=open('n4.txt','r+')     # 0
# print(f.tell())

# f=open('n4.txt','a+')          
# print(f.tell())


# f=open('n4.txt','r+')    
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())


#    seek() -
# ----------------

# syntex :-   
#             seek('how many bits are move','from where')
#                                            ----------
#                       starting position  <---  0 |         
#                  |---  current position  <---  1 |         
#       binary <---|---     last position  <---  2 |                
#       ------                                                                           
#          |                  _______                               
#          |----------------- | xb+ |
#                             | wb+ |
#                             | rb+ |
#                             | ab+ |
#                             |_____|                  




# f=open('n3.txt','rb+')
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())
# f.seek(-5,1)
# print(f.tell())
# f.read(10)
# print(f.tell())




f=open('n3.txt','rb+')
data=f.read(25)
f.seek(20)
print(f.tell())
f.seek(-1,2)
print(f.tell())
f.seek(-5,2)
data=f.read()
print(data)
