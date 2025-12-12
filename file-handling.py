
# major operation in file-handling

#    1.  create()/open()
#    2.  write()/read()
#    3.  close()



#   1. open() :-
# ----------------------------------------------------------------------
            #    syntex -    open('filename with , mode extension')


 #                                                mode 
 #                                                  |
 #                                                  |------  x - (create)
 #                                                  |------  w - (write)
 #                                                  |------  r - (read)                      
 #                                                  |------  a - (append)
               



# f=open('n1.txt','x')



# f=open('n2.txt','x')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)




# f=open('n2.txt','w')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)


# ---------------------------------------------------------------------------------------------------------------

# | mode  |   create-new    |     exist-file   |   writable   |     readable    |      cursor-position
# |  x    |      yes        |       no         |    yes       |       no        |        0th-index               
# |  w    |      yes        |       yes        |    yes       |       no        |       0th-index  
# |  r    |       no        |       yes        |    no        |      yes        |         0th-index              
# |  a    |      yes        |       yes        |    yes       |       no        |      previous-last          

# ---------------------------------------------------------------------------------------------------------------

# | mode  |   create-new    |     exist-file   |   writable   |     readable    |      cursor-position
# |  x+   |      yes        |       no         |    yes       |      yes        |        0th-index               
# |  w+   |      yes        |       yes        |    yes       |      yes        |       0th-index  
# |  r+   |       no        |       yes        |    yes       |      yes        |         0th-index              
# |  a+   |      yes        |       yes        |    yes       |      yes        |      previous-last          

# ----------------------------------------------------------------------------------------------------------------


# f=open('n2.txt','x+')
# f=open('n2.txt','w+')
# f=open('n2.txt','r+')
# f=open('n2.txt','a+')




# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*


# write   -----
#             | ---- write()
 #            | ---- writelines()


# write() --
# -----------------

# f=open('n3.txt','a+')
# data='this is python class \n'      # \n use for new line 
# f.write(data)
# f.close()



# writelines() --
# --------------------

# f=open('n3.txt','a+')
# data=['python\n','java\n','PHP\n'] 
# f.writelines(data)


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*


# read  -----
#             | ---- read()  -- read all data
 #            | ---- read(n)  -- read n-bits of data
#             | ---- readline()  -- read single-line of data
#             | ---- readlines()  -- read all-line of data 



# read() --
# -------------

# f=open('n3.txt', 'r+')
# data=f.read()
# print(data)
# f.close()


# read(n) --
# ---------------

# f=open('n3.txt', 'r+')
# data=f.read(10)
# print(data)
# # f.close()
# data=f.read(5)
# print(data)


# f=open('n3.txt', 'r+')
# data=f.read()
# print( "first : " ,data)
# # f.close()
# data=f.read(5)
# print("last : " ,data)


# readline() --
# -------------------

# f=open('n3.txt', 'r+')
# data=f.readline()                      # it read single-line data
# print(data)
# f.close()


# readlines() --
# -------------------

# f=open('n3.txt', 'r+')
# data=f.readlines()                      # it read all-line code
# print(data)
# f.close()