# 練習問題19.6
# コルセルトの判定法を用いて、カーマイケル数かどうかを判断する


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




# コルセルトの判定
def Korselt_judgement(n):
    # 偶数なら、カーマイケル数ではない
    if (n % 2 == 0):
        return False


    decomp = factorization(n)

    # 指数部分に1以外があれば、カーマイケル数ではない
    if ( decomp[1].count(1) != len(decomp[1]) ):
        return False

    # 素数ならカーマイケル数ではない
    if ( len(decomp[0]) == 1 ):
        return False

    # p-1がn-1をわらないなら、カーマイケル数ではない
    for frac in decomp[0]:
        if ( (n - 1) % (frac - 1) != 0 ):
            return False

    return True




# n = int( input("正の数を入力(終了は-1)：") )
# while ( n > 0 ):
#     if (Korselt_judgement(n)):
#         print("カーマイケル数です")
#     else:
#         print("カーマイケル数ではありません")

#     n = int( input("正の数を入力(終了は-1)：") )


# 100000までのカーマイケル数のリスト
Carmichael_list = []
for i in range(1, 100000, 2):
    if (Korselt_judgement( i )):
        Carmichael_list.append(i)
        print(i)

print(Carmichael_list)

# 1000000を超える最小のカーマイケル数
# i = 1000001

# while ( not Korselt_judgement(i)):
#     i += 2

# print(i)
