def multiplyList(*arr):
    res = 1
    for i in arr:
        res *= i
    return res
    
arr = list(map(int, input().split()))
print(multiplyList(*arr))