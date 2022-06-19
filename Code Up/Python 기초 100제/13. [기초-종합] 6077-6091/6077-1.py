import sys
n=int(sys.stdin.readline())
sum=0
i=1
while i<n+1:
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)