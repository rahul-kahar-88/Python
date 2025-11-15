

# ============================= frozenset ===================================

# = collection of unique element
# = represented by frozenset({}) with comma (,) seperated element
# = unordered collection 
# = indexing not supported
# = slicing not supported
# = immutable in nature



# s = 'python'
# l = [10,20,30,'python']
# t=[1,2,3,4,'python']

# fs1=frozenset(s)
# print(fs1,type(fs1))
# # fs2=frozenset(l)
# # print(fs2,type(fs2))
# # fs3=frozenset(t)
# # print(fs3,type(fs3))

# print(len(fs1))
# print(type(fs1))
# print(id(fs1))
# print(fs1)
# print(min(fs1))
# print(sum(fs1))
# print(max(fs1))




# method ------
# 1 - union , 2 - intersection , 3 - difference , 4 - symmetric_difference , 5 - isdisjoint , 6 - issuperset , 7 - issubset 

fs1 = frozenset({1,2,3,4,5})
fs2 = frozenset({4,5,6,7,8})

print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issuperset(fs2))
print(fs1.issubset(fs2))










