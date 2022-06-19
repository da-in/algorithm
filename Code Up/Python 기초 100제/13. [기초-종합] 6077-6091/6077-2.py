import sys
n=int(sys.stdin.readline())
if(n%2==0):
    print(int(n*(n+2)/4))
else:
    print(int((n-1)*(n+1)/4))

# 실행시간은 6077-1.py 가 더 빠르다.