import copy
my_list=[[1,2,3],[1,2,3],[1,2,3]]
s_list = copy.copy(my_list)
print(s_list)
#s_list=copy.deepcopy(my_list)
#print(s_list)
s_list.remove([1,2,3])
print(s_list)
print(my_list)