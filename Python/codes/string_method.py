# find(x)
print('banana'.find('a'))       # 1 (첫 번째 위치 반환)
print('banana'.find('z'))       # -1

# index(x)
print('banana'.index('a'))      # 1
print('banana'.index('z'))      # ValueError: substring not found

# isupper() / islower() / isalpha()
string1 = 'HELLO'
string2 = 'Hello'
string3 = '123'

print(string1.isupper())        # True
print(string2.isupper())        # False
print(string1.islower())        # False
print(string2.islower())        # False
print(string1.isalpha())        # True
print(string3.isalpha())        # False