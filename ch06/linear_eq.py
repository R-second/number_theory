### 練習問題6.3

# (b), (d), (e)
# 一次方程式 ax+by=gcd(a,b) の整数解を求めるプログラム
def linear_eq(a, b):
    # bが0もしくは、aが0のとき
    if b == 0:
        return (a, 1, 0)
    if a == 0:
        return (b, 0, 1)

    # 初期状態
    x = 1
    g = a
    v = 0
    w = b

    # wが0になるまで繰り返す.
    while w != 0:
        q = g // w        # g/w の整数部分
        t = g - q * w       # g/w の余り t

        s = x - q * v
        x = v
        g = w

        v = s
        w = t
        # print(w)

    y = (g - a * x) // b

    while x <= 0:
        x = x + b
        y = y - a

    return (g, x, y)



# (c)
print(linear_eq(19789, 23548))
print(linear_eq(31875, 8387))
print(linear_eq(22241739, 19848039))



