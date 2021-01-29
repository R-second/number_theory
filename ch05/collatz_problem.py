### 「3n+1」アルゴリズム

# 入力nから、「3n+1」アルゴリズムに従う次の数字を返す
def collatz_next(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


# アルゴリズムの長さL(n)と、最後の値T(n)を返す
def collatz(n):
    # 生成された数列を格納
    sequence = [n]

    next_num = collatz_next(n)

    while next_num not in sequence:
        sequence.append(next_num)
        next_num = collatz_next(next_num)

    return len(sequence), int(sequence[-1])      # 配列の要素数と末尾の値を返す




# 入力用
choice = int(input("表の出力は0, あるnに対して L(n)とT(n)を求めたいときは1を入力してください："))

if choice == 0:
    print(" n | L(n) | T(n) ")
    print("-----------------")
    for i in range(1, 101):
        (L, T) = collatz(int(i))
        print("{0:>3}|{1:>6}|{2:>6}".format(i, L, T))

elif choice == 1:
    n = input("整数を入力してください：")
    (L, T) = collatz(int(n))

    print("L({0})={1}, T({0})={2}".format(n, L, T))

else:
    print("適切な入力ではありません.")









