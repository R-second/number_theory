# 練習問題11.8
# 連立合同式を解く


# 一次方程式 ax+by=gcd(a,b) の整数解を求めるプログラム
# cf: ../ch06/linear_eq.py
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

    y = (g - a * x) // b

    while x <= 0:
        x = x + b
        y = y - a

    return (g, x, y)


# 連立合同式 x = b (mod m), x = c (mod n) の解を求める.
# gcd(m, n) = 1
def solve_sim_congruence(b, m, c, n):
    g, x, y = linear_eq(m, n)
    print(x)

    y_1 = int( (c - b) * x )

    x_0 = y_1 * m + b

    # 解は正で出力
    while x_0 < 0:
        x_0 = x_0 + m * n

    return x_0


# 実験
print( solve_sim_congruence(3, 7, 5, 9) )
print( solve_sim_congruence(3, 37, 1, 87) )



