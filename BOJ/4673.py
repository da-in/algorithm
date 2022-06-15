def d(n):
    num = list(map(int, str(n)))
    return(n+sum(num))


results = list(range(1, 10001))

for i in range(1, 10001):
    temp = d(i)
    if(temp in results):
        results.remove(temp)

for result in results:
    print(result)
