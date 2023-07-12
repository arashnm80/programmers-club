n, m = map(int, input().split())

k = 1
for i in range(n):
    line = range(k, m+k)
    if i % 2 == 1:
        line = reversed(line)
    line = list(line)
    line = " ".join(map(str,line))
    print(line)
    k = k + m