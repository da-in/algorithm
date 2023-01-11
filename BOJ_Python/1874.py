L = int(input())
increase = 1
stack = [0]
answer = []
available = True

for i in range(L):
    n = int(input())
    while (1):
        if (stack[-1] == n):
            stack.pop()
            answer.append('-')
            break
        elif (stack[-1] < n):
            stack.append(increase)
            answer.append('+')
            increase += 1
        else:
            available = False
            break
    if (not available):
        break

if (available):
    print('\n'.join(answer))
else:
    print('NO')
