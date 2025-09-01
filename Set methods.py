# set - Collection of numbers/characters/stings which will not have a duplicate values.
#  It is mutable. This will not support indexing

# Builtin functions/methods are given below

# add
# remove
# union
# intersection 
# difference

set1 = {1,3,5,7,9}
set1.add(79)
print(set1)

set1 = {1, 3, 5, 7, 9, 79}
set1.add(1022)
print(set1)

set1 = {1, 3, 5, 7, 9, 1022, 79}
set1.remove(7)
print(set1)

set1 = {1,2,3,4,5,6}
set2 = {10,11}
D = set1.union(set2)
print(D)

set1 = {1,2,3,4,5}
set2 = {1,2,3,7,8}
D=set1.intersection(set2)
print(D)

set1 = {1,2,3,4,5}
set2 = {1,2,3,7,8}
D=set1.difference(set2)
print(D)