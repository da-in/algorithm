#python 3항 연산자를 사용한 방법
import sys
a, b, c = sys.stdin.readline().split()
a = int(a)
b = int(b)
c = int(c)

print((a if a<=b else b) if (a if a<=b else b)<=c else c)