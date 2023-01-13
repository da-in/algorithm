# Do it! Python 코딩테스트 준비 : 선택정렬로 풀기
N = input()
N = list(map(int, list(N)))
length = len(N)

for i in range(length-1):
    temp = N[i: length]
    max_index = temp.index(max(temp))+i
    N[i], N[max_index] = N[max_index], N[i]


for n in N:
    print(n, end='')
