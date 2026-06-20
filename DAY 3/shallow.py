import sys
my_list=[10,20,30,40]
print(list.__sizeof__(my_list))
print(sys.getsizeof(my_list))
print(my_list)
s_list=(my_list)
s_list[3]=14
print(f"Original List:{s_list}")
print(f"Copied List:{my_list}")

