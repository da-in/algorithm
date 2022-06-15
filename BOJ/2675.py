n = int(input())
for i in range(0, n):
    a, b = input().split()
    a = int(a)
    b = list(b)
    for c in b:
        print(c*a, end="")
    print()
