#SET Common Usecase
# new_set = {1,2,3,4}
# print(new_set)
# print(type(new_set))
#
# new_set.add(100)
# print(new_set)
#
# new_set.discard(4)
# print(new_set)
#
# new_set.remove(1)
# print(new_set)
#
#UNION
# set1={1,2,3}
# set2={3,4,5}
# union_set = set1.union(set2)
# union_set_pipe = set1 | set2
# print(union_set)
# print(union_set_pipe)
#
# int_set=set1.intersection(set2)
# print(int_set)
#
# diff_set = set1.difference(set2)
# print(diff_set)

#Square with comprehension
squares = {x**2 for x in range(1,5)}
print(squares)
