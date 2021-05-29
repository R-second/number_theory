# 練習問題16.4

import random

# 繰り返し二乗法で, a^k (mod m) を求める. (power_mod.py)
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = a * a
        k = int(k / 2)
    return b


## 擬素数かどうかのチェック
def is_pseudoprime(n):
    for i in range(0, 10):
        a = random.randint(2, n-1)
        if power_mod(a, n-1, n) != 1:
            print("nは合成数")
            return False

    print("nは擬素数")
    return True



# 実験
is_pseudoprime(9991)
is_pseudoprime(17)      # 素数
is_pseudoprime(561)     # カーマイケル数




