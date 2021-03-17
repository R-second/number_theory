### 練習問題8.7


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


### 一次合同式 ax=c (mod m) を解く
def solve_congruence(a, c, m):
    # 一次方程式を解く
    g, x, y = linear_eq(a, m)
    if c % g != 0:  # 解なし
        return (g, [])
    else:
        x = int(c * x / g)
        solutions = [ int(x +  i * m / g) for i in range(0, g) ] # すべての解をピックアップ
        return (g, solutions)


# 解のリストを適切な表式で出力
def print_solutions(a, c, m):
    # 合同式を解く
    g, solutions = solve_congruence(a, c, m)

    if not solutions:   # 解なしなら、解のリストは空
        print("合同式 {0}x = {1} (mod {2}) の解はありません".format(a, c, m))

    else:
        # すべての解がm以下になるように整形し、並べ替え
        for key, sol in enumerate(solutions):
            while sol >= m:
                sol -= m
            solutions[key] = sol

        solutions.sort()

        # 出力
        print("合同式 {0}x = {1} (mod {2}) の解は以下の{3}個です.".format(a, c, m, g))
        print("x = " ,end="")
        for sol in solutions:
            print("{0}".format(sol), end=", ")
        print("(mod {0})".format(m))



print_solutions(8, 6, 14)
print_solutions(66, 100, 121)
print_solutions(21, 14, 91)

