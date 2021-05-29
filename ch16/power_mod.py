# 練習問題16.2

# 繰り返し二乗法で, a^k (mod m) を求める.
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = a * a
        k = int(k / 2)
    return b


# (c) 計算
print(power_mod(2, 1000, 2379))
print(power_mod(567, 1234, 4321))
print(power_mod(47, 258008, 1315171))


# 16.1 の確認
# print(power_mod(5, 13, 23))
# print(power_mod(28, 749, 1147))

# 16.3
# print(power_mod(7, 7386, 7387))
# print(power_mod(7, 7392, 7393))

# 16.5
# print(power_mod(2, 9990, 9991))
