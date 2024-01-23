my_list = [1, 2, 3]
index = my_list.index(2)
print(index)        # 1

my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count)        # 3

my_list = [3, 2 ,1]
my_list.sort()
print(my_list)      # [1, 2, 3]

# 내림차순
my_list.sort(reverse=True)
print(my_list)      # [3, 2, 1]

my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)      # [9, 1, 8, 2, 3, 1]