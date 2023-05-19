n = int(input())
s = input()
s = [int(x) for x in s.split()]
s.sort()

h_index = 0

for i in range(n):
    if n - i <= s[i]:
        h_index = n - i
        break

print(h_index)