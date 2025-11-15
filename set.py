# set()
# ======================================================================================================================================================

# - collection of unique element
# - represented by {} with comma(,) seperated element
# - unorded collection
# - indexing not supported
# - slicing not supported
# - mutable in nature




# my_set = {10,20,30,'java','php','python'}
# print(type(my_set))
# print(id(my_set))
# # print(min(my_set))    --|
# # print(sum(my_set))    --|------- error
# # print(max(my_set))    --|
# print(my_set)
# print(len(my_set))



# set method -------------------------


# # 1 = union()--------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# print(s1.union(s2))



# # 2 = intersection()--------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# print(s1.intersection(s2))



# # 3 = difference--------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# print(s1.difference(s2))



# # 4 = symmetric_difference----------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# print(s1.symmetric_difference(s2))



# # 5 = intersection_update----------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# s1.intersection_update(s2)
# print(s1)
# print(s2)

# # print(s2)
# # print(s1)



# # 6 = difference_update----------
# s1,s2={1,2,3,4,5},{4,5,6,7,8}
# s1.difference_update(s2)
# print(s1)
# print(s2)




# 8 = issuperset()--
# s1,s2={1,2,3,4,5,6,7,8},{5,6,7,8}
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))



# issubset()--
# s1,s2={1,2,3,4,5,6,7,8},{5,6,7,8}
# print(s1.issubset(s2))
# print(s2.issubset(s1))



# 10 =  isdisjoint()--
# s1,s2={1,2,3,4},{5,6,7,8}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s1))

# s1,s2={1,2,3,4,5},{5,6,7,8}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s1))





# s={1,2,3,"java","python"}
# s1 = s.copy()
# print(s1)
# print(id(s1),id(s))


# s={1,2,3,"java","python"}
# s.clear()
# print(s)
# del



# s={1,2,3,'java','python'}
# s.add('php')
# print(s)


# s={1,2,3,'java','python'}
# s.update({6,5,4,3})
# print(s)


# s={1,2,3,'java','python'}
# print(s.pop())


# s={1,2,3,'java','python'}
# s.remove('python')
# print(s)



s={1,2,3,'java','python'}
s.discard('rahul')
print(s)










