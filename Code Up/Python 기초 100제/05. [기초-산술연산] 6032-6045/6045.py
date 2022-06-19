from array import array
import sys
num = list(map(int, sys.stdin.readline().split()))

print(sum(num), format(sum(num)/len(num), ".2f"))