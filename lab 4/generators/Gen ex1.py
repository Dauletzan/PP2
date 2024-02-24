def gensquares(N):
    for x in range(1, N+1):
        yield x**2
for x in gensquares(10):
    print(x)