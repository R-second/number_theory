# 練習問題12.1
# プログラムで実装

import math

# 2から1000までの素数
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997 ]

# nの(素因数)分解を返す (ch07より引用)
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


prime_list = [5]

while len(prime_list) < 9:
    A = 1
    for prime in prime_list:
        A *= prime
    A += 1

    decomp = factorization(A)
    for index, frac in enumerate(decomp[0]):
        if frac not in prime_list:
            prime_list.append(frac)
            break
    print(prime_list)


