## 練習問題17.6
# x^k = b (mod m)を解く (bのk乗根)

import math

# 2から1000までの素数
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997 ]

# nの(素因数)分解を返す (cf: ch07)
def factorization(n):
    limit = math.sqrt(n)

    # nの分解を表す行列 (decomp[0]が約数, decomp[1]がその個数)
    decomp = [[], []]

    # 2から1000までの素数のみで調べてスピードアップを図る
    for i in primes:
        while n % i == 0:
            if i in decomp[0]:
                decomp[1][decomp[0].index(i)] += 1
            else:
                decomp[0].append(i)
                decomp[1].append(1)
            n = int(n / i)

    # 1009以上の素数で割れないか調べる
    i = 1009
    while i <= limit:
        while n % i == 0:
            if i in decomp[0]:
                decomp[1][decomp[0].index(i)] += 1
            else:
                decomp[0].append(i)
                decomp[1].append(1)
            n = int(n / i)

        i += 1

    # リストに何も追加されていなければ
    if n != 1:
        decomp[0].append(n)
        decomp[1].append(1)

    return decomp



# オイラーのファイ関数 (cf: ch11)
def phi(m):
    decomp = factorization(m)

    result = 1

    for index, frac in enumerate(decomp[0]):
        result *= (frac - 1) * frac ** (decomp[1][index] - 1)

    return result


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


### 一次合同式 ax=c (mod m) を解く (cf: ch8)
def solve_congruence(a, c, m):
    # 一次方程式を解く
    g, x, y = linear_eq(a, m)
    if c % g != 0:  # 解なし
        return (g, [])
    else:
        x = int(c * x / g)
        solutions = [ int(x +  i * m / g) for i in range(0, g) ] # すべての解をピックアップ
        return (g, solutions)


# 繰り返し二乗法で, a^k (mod m) を求める. (cf: ch16)
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = ( a * a ) % m
        k = int(k / 2)
    return b


# x^k = b (mod m)を解く (bのk乗根)
def kth_root(k, b, m):
    # Step1. phi(m)
    phi_m = phi(m)

    # Step2. ku = 1 (mod phi(m))を解く
    (g, solutions) = solve_congruence(k, 1, phi_m)

    # Step3. b^u (mod m) を求める
    return power_mod(b, solutions[0], m)


print( kth_root(131, 758, 1073) )
print( kth_root(329, 452, 1147) )   # 17.1
print( kth_root(113, 347, 463) )   # 17.2(a)
print( kth_root(275, 139, 588) )   # 17.2(b)





