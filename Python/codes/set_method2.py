set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))        # {0, 2, 4}
print(set1.intersection(set2))      # {1, 3}
print(set1.issubset(set2))          # False
print(set1.issuperset(set2))        # False
print(set1.union(set2))             # {0, 1, 2, 3, 4, 5, 7, 9}