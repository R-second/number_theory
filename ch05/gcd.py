### 最大公約数を求めるプログラム
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    q = a // b
    r = a - q * b       # a/b の余り r

    if r == 0:
        return b
    else:
        return gcd(b, r)




### いくつか実験
print(gcd(36, 132))
print(gcd(12345, 67890))
print(gcd(54321, 9876))

# 0を含む場合
print(gcd(0, 56))
print(gcd(34, 0))

# 負数を含む場合
print(gcd(-36, 132))
print(gcd(12345, -67890))
print(gcd(-54321, -9876))

