text = 'Hello, world!'
new_text = text.replace('world','Python')
print(new_text)                 # Hello, Python!

text = '    Hello, world!    '
new_text = text.strip()
print(new_text)                 # Hello, world!

text = 'Hello, world!'
words = text.split(',')
print(words)                    # ['Hello', ' world!']

words = ['Hello', 'world!']
text = '-'.join(words)
print(text)                     # Hello-world!

text = 'heLLo, woRld!'
new_text1 = text.capitalize()   # Hello, world!
new_text2 = text.title()        # Hello, World!
new_text3 = text.upper()        # HELLO, WORLD!
new_text4 = text.swapcase()     # HEllO, WOrLD!

print(new_text1)
print(new_text2)
print(new_text3)
print(new_text4)

# 메서드 이어서 사용 가능
# but 리턴값이 None인 메서드는 이어서 사용하지 못함!
new_text = text.swapcase().replace('l','z')
print(new_text)                 # HEzzO, WOrLD!