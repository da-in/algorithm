def reverse(n):
    return(n[::-1])


nums = map(reverse, input().split())
print(max(nums))
