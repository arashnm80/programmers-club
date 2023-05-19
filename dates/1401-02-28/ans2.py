n = int(input())
s = input()
s = [int(x) for x in s.split()]
s.sort()

mx = max(s)
h_index = 0

for i in range(mx):
    count = 0
    for j in range(n):
        if s[j] >= i:
            count += 1
    if count == i:
        if count > h_index:
            h_index = count

print(h_index)