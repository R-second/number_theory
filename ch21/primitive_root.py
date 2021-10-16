### 練習問題21.11
### 素数pに対して原始根を求める


# 繰り返し二乗法で, a^k (mod m) を求める.
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = ( a * a ) % m
        k = int(k / 2)
    return b



# 指数e_p(a)を求める
def index_e(p, a):
    for e in range(1, int(p/2) + 1):
        if power_mod(a, e, p) == 1:
            return e

    return p - 1


# 原始根を求める
def primitive_root(p):
    for i in range(2, p):
        if index_e(p, i) == p - 1:
            return i



n = int( input("素数を入力(終了は-1)：") )
while ( n > 0 ):
    print("{0}の原始根：{1}".format(n, primitive_root(n)))

    n = int( input("素数を入力(終了は-1)：") )








