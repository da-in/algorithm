import sys
a, m, d, n = map(int, sys.stdin.readline().split())
# 갑자기 일반항을 구해보고 싶었다.
# n과 m이 1일경우 예외처리 필요.
# print(int((a+(d/(m-1)))*(m**(n-1))-(d/(m-1))))
for i in range(0,n-1):
    a=a*m+d
print(a)