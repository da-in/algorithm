word = input()
count = 0
a = ord('A')
for w in word:
    temp = ord(w)
    if(w == 'Z'):
        count = count+((temp-a-1)//3)+2
    elif(temp >= ord('S')):
        count = count+((temp-a-1)//3)+3
    else:
        count = count+((temp-a)//3)+3
print(count)
