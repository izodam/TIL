# add-------------------------------------------
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)       # {'c', 1, 2, 3, 4, 'b', 'a'}
print(my_set)

my_set.add(4)       # {'c', 1, 2, 3, 4, 'b', 'a'}
print(my_set)

# clear()-------------------------------------------------
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set)       # set()

# remove-------------------------------------------------
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.remove(2)
print(my_set)            # {1, 3, 'a', 'b', 'c'}

my_set.remove(10)
print(my_set)            # KeyError: 10

# discard-------------------------------------------------
my_set = {1, 2, 3}

my_set.discard(2)
print(my_set)           # {1, 3}

my_set.discard(10)      # 에러 없음

# pop-------------------------------------------------
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()

print(element)          # 1
print(my_set)           # {2, 3, 'b', 'a', 'c'}

# update-------------------------------------------------
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set)           # {1, 2, 3, 'c', 4, 5, 'b', 'a'}