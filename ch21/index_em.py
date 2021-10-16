### 練習問題21.14
### e_m(a)を求める.

# 繰り返し二乗法で, a^k (mod m) を求める.(cf. ch16)
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = ( a * a ) % m
        k = int(k / 2)
    return b


# 指数e_m(a)を求める
def index_em(m, a):
    for e in range(1, m):
        if power_mod(a, e, m) == 1:
            return e




m = int( input("数を入力：") )

n = int( input("正の数を入力(終了は-1)：") )
while ( n > 0 ):
    print("{0}を法とした{1}の最小の指数：{2}".format(m, n, index_em(m, n)))

    n = int( input("正の数を入力(終了は-1)：") )





