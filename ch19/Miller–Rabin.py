# 練習問題19.7
# ラビンミラー判定法


# 繰り返し二乗法で, a^k (mod m) を求める. (cf: ch16)
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = ( a * a ) % m
        k = int(k / 2)
    return b



# 合成数ならTrue, そうでない可能性が高いならFalse
def Miller_Rabin_judgement(n):
    if (n % 2 == 0):
        return True

    # n-1 = 2^k * q なるk, qを求める
    q = n - 1
    k = 0
    while( q % 2 == 0 ):
        q /= 2
        k += 1

    a = 2

    if( power_mod(a, q, n) == 1 ):
        return False

    index = q
    for i in range(0, k):
        if( power_mod(a, index, n) == n-1 ):
            return False
        index = 2 * q

    return True






n = int( input("正の数を入力(終了は-1)：") )
while ( n > 0 ):
    if (Miller_Rabin_judgement(n)):
        print("合成数です")
    else:
        print("素数である可能性が高いです")

    n = int( input("正の数を入力(終了は-1)：") )




