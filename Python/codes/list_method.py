my_list = [1, 2, 3]
my_list.append(4)
print(my_list)      # [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)      # [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)      # [1, 5, 2, 3]

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)      # [1, 3]

my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)        # 5
print(item2)        # 1
print(my_list)      # [2, 3, 4]

my_list = [1, 2, 3]
my_list.clear()
print(my_list)      # []