word = input().upper()
char = set(word)
result = ''
count = 0
for c in char:
    if(word.count(c) > count):
        result = c
        count = word.count(c)
    elif(word.count(c) == count):
        result = '?'
print(result)
