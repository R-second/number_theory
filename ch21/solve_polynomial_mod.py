### 練習問題21.12
### f(X)=0 (mod m)を解く

# f(a) mod m の値を求める
def polynomial_mod(a, coeffiient_list, m):

    f_val = 0   # fの値
    a_pow = 1   # ベキの値
    for c in coefficient_list:
        f_val = (f_val + c * a_pow % m) % m
        a_pow = (a_pow * a) % m

    return f_val


# 多項式の方程式 f(X) = 0 (mod m) を解く
def solve_pol(coefficient_list, m):
    # 全て0〜m-1の間に
    coefficient_list = [ c % m for c in coefficient_list]

    solution = []

    # しらみつぶし
    for i in range(0, m):
        if polynomial_mod(i, coefficient_list, m) == 0:
            solution.append(i)

    return solution



m = int( input("mを入力:") )
coefficient_list = input("昇ベキの順に係数をカンマ区切りで入力：")
coefficient_list = coefficient_list.replace(' ', '')
coefficient_list = coefficient_list.split(',')
coefficient_list = [ int(c) for c in coefficient_list]

print( solve_pol(coefficient_list, m) )



