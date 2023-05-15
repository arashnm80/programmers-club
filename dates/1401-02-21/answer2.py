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
text = input()
n, s, d = [int(x) for x in text.split()]

s_ru = get_ru(n, s)
d_ru = get_ru(n, d)

print("R: ", d_ru[0] - s_ru[0])
print("U: ", d_ru[1] - s_ru[1])

# توضیح بیشتر درباره متغیر ها:
# Shift = تعداد لایه ای که جابجا شده بود
# S = تعداد اعدادی که تا اون لایه مدنظر ما پوشش میده مثلا لایه اول شانزده تا عدد اول رو پوشش میده
# P = وقتی ی پارامتر میخواییم به تابع پاس بدیم کار تابع پیدا کردن مختصات بود
# N = ضلع مربع
# L = left
# R = right 
# U = up
#Dif = difference
