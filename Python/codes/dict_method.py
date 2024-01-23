# clear-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
person.clear()
print(person)                           # {}

# get-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
print(person.get('name'))               # Alice
print(person.get('country'))            # None
print(person.get('country', 'Unknown')) # Unknown

# keys-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
print(person.keys())                    # dict_keys(['name', 'age'])

for k in person.keys():
    print(k)
'''
name
age
'''

# values-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
print(person.values())                  # dict_values(['Alice', 25])

for v in person.values():
    print(v)
'''
Alice
25
'''

# items-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
print(person.items())               # dict_items([('name', 'Alice'), ('age', 25)])

for k,v in person.items():
    print(k, v)
'''
name Alice
age 25
'''

# pop-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}

print(person.pop('age'))                # 25
print(person)                           # {'name' : 'Alice'}
print(person.pop('country', None))      # None
# print(person.pop('country'))            # keyError

# setdefault-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}

print(person.setdefault('country', 'KOREA'))    # KOREA
print(person)               # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update-------------------------------------------------
person = {'name' : 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)               # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age = 50)
print(person)               # {'name': 'Jane', 'age': 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person)               # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}