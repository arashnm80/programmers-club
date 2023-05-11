def get_ru(n, p):
    if n * n == p:
        return [n // 2 + 1, n // 2 + 1]
    s = 0
    l = n
    shift = 0
    while(s <= n * n):
        s += 4 * (l - 1)
        if s >= p:
            break
        else:
            shift += 1
            l -= 2
    
    dif =(4 * (l - 1)) - (s - p)
    step = 0
    r, u = 0, 1
    while True:
        step += 1
        if 1 <= step <= l:
            r += 1
        elif l < step <= 2 * l - 1:
            u += 1
        elif 2 * l - 1 < step <= 3 * l - 2:
            r -= 1
        else:
            u -= 1

        if step == dif:
            return [r + shift, u + shift]

# print(get_ru(5, 25))

text = input()
n, s, d = [int(x) for x in text.split()]

s_ru = get_ru(n, s)
d_ru = get_ru(n, d)

print("R: ", d_ru[0] - s_ru[0])
print("U: ", d_ru[1] - s_ru[1])