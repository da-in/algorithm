import math
a, b, c = map(float, input().split())
if(c <= b):
    print(-1)
else:
    print(math.floor(a/(c-b))+1)
