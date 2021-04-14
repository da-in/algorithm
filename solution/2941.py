croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for temp in croatia:
    word = word.replace(temp, '*')
print(len(word))