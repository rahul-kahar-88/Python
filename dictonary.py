#dictonary
#=======================================================================================================================================================


#d = { 'name':'rahul' , 'age':20 , 'qual':'bca'}
#print(type(d))
#print(len(d))
#print(id(d))
#print(d)
#print(max(d))
#print(min(d))
#print(sum(d))


#d = { 1:'rahul' , 2:20 , 3:'bca'}
#print(sum(d))




#method
#-----------------------
#copy()  , clear() ,  get()   - d.get('name') , values() , kays() ,  items() ,  fromkeys() , update() , pop() , popitem() 

# d = { 'name':'rahul' , 'age':20 , 'qual':'bca'}
# d1 = d.copy()
# print(d,d1)
# print(id(d),id(d1))


# d1 = d.clear()
# print(d)
# del d 
# print(d)



# d = { 'x':10 , 'y':20 , 'z':30}
# print( d.get('x'))

# print( d.keys())

# print( d.values())

# print(d.items())

# print(d.pop('y'))
# print(d)

# d.popitem()
# print(d)



# fromkeys()===============================

# s=[10,20,30,'python']
# d = dict.fromkeys(s,100)
# print(d)



# s=['name','email','contact','address']
# d = dict.fromkeys(s)
# n = 'rahul'
# e = 'rahulkahar@gmail.com'
# c = 12345678
# a = 'gorakhpur'
# # d['key']=update_value
# d['name'] = n
# d['email'] = e
# d['contact'] = c
# d['address'] = a
# print(d)




# update()=================================


# d1 = {'x':10,'y':20}
# d2 = {'z':30}
# d1.update(d2)
# print(d1)   #updated dict
# print(d2)   #old dict



# setdefault()=============================
# d={'x':10,'y':20}
# # print(d.setdefault('x',30))
# print(d.setdefault('z',30))
# print(d)

