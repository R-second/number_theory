# 練習問題18.5
# RSA暗号の暗号化と復号化

# gcd(a, b)と、一次方程式 ax+by=gcd(a,b) の整数解を同時に求めるプログラム (ch06)
def linear_eq(a, b):
    # bが0もしくは、aが0のとき
    if b == 0:
        return (a, 1, 0)
    if a == 0:
        return (b, 0, 1)

    # 初期状態
    x = 1
    g = a
    v = 0
    w = b

    # wが0になるまで繰り返す.
    while w != 0:
        q = g // w        # g/w の整数部分
        t = g - q * w       # g/w の余り t

        s = x - q * v
        x = v
        g = w

        v = s
        w = t

    y = (g - a * x) // b

    while x <= 0:
        x = x + b
        y = y - a

    return (g, x, y)



# 一次合同式 ax=c (mod m) を解く
def solve_congruence(a, c, m):
    # 一次方程式を解く
    g, x, y = linear_eq(a, m)
    if c % g != 0:  # 解なし
        return (g, [])
    else:
        x = int(c * x / g)
        solutions = [ int(x +  i * m / g) for i in range(0, g) ] # すべての解をピックアップ
        return (g, solutions)


# 繰り返し二乗法を用いて a^k (mod m) を求める
def power_mod(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a * b) % m
        a = ( a * a ) % m
        k = int(k / 2)

    return b




# x^k = b (mod m)を解く (bのk乗根) (ただし、ファイ関数の値は与える.)
def kth_root(k, b, m, phi):
    # Step1. phi(m)
    # 略

    # Step2. ku = 1 (mod phi(m))を解く
    (g, solutions) = solve_congruence(k, 1, phi)

    # Step3. b^u (mod m) を求める
    return power_mod(b, solutions[0], m)



encrypt_table = {'A':'11', 'B':'12', 'C':'13', 'D':'14', 'E':'15', 'F':'16', 'G':'17', 'H':'18', 'I':'19', 'J':'20', 'K':'21', 'L':'22', 'M':'23', 'N':'24', 'O':'25', 'P':'26', 'Q':'27', 'R':'28', 'S':'29', 'T':'30', 'U':'31', 'V':'32', 'W':'33', 'X':'34', 'Y':'35', 'Z':'36', ' ':'37', ',':'38', '.':'39'}


decrypt_table = {'11':'A', '12':'B', '13':'C', '14':'D', '15':'E', '16':'F', '17':'G', '18':'H', '19':'I', '20':'J', '21':'K', '22':'L', '23':'M', '24':'N', '25':'O', '26':'P', '27':'Q', '28':'R', '29':'S', '30':'T', '31':'U', '32':'V', '33':'W', '34':'X', '35':'Y', '36':'Z', '37':' ', '38':',', '39':'.'}

# 暗号化
# 文字列の暗号化ルール：A->11, B->12, ... Z->36, 空白->37, ,->38, .->39 それ以外->40
# 大文字・小文字は区別しない
def encrypt(message, m, k):
    message = message.upper()
    cypher_pre = ""
    for ch in message:
        cypher_pre += encrypt_table[ch]

    m_length = len(str(m))
    cypher_length = len(cypher_pre)

    # mの桁 - 1桁ずつ区切る
    blocks = [ cypher_pre[i : i + m_length - 1] for i in range(0, cypher_length, m_length - 1)]


    cypher = []
    for block in blocks:
        cypher.append( power_mod(int(block), k, m))

    print(cypher)

    return cypher


# 復号化
# カンマ区切りの文字列
def decrypt(cypher_txt, p, q, k):
    cypher_txt = cypher_txt.replace(' ', '')
    cypher_list = cypher_txt.split(',')

    message_num = ""

    for code in cypher_list:
        message_num += str( kth_root(k, int(code), p * q, (p - 1)*(q - 1)) )

    message = ""
    for i in range(0, len(message_num), 2):
        message += decrypt_table[ message_num[i : i+2] ]


    return message



if __name__ == '__main__':

    print("鍵を生成します. 2つのなるべく大きな素数を入力してください：")
    p = int( input("1つ目：") )
    q = int( input("2つ目：") )
    m = p * q

    phi = (p - 1) * (q - 1)
    k = int( input("指数k({}と互いに素な数)：".format(phi)) )

    flag_decrypt = int( input("暗号化は0, 復号化は1：") )

    if flag_decrypt == 0:    # 暗号化(encrypt)
        message = input("暗号化したいメッセージ：")

        cypher = encrypt(message, m, k)
        print(cypher)


    elif flag_decrypt == 1:   # 復号化(decrypt)
        cypher_txt = input("復号化したい暗号(カンマ区切りでスペースなし)：")

        message = decrypt(cypher_txt, p, q, k)

        print(message)

    else:
        print("0か1を入力してください")



# 73 * 97 = 7081

# 5272281348, 21089283929, 3117723025, 26844144908, 22890519533, 26945939925, 27395704341, 2253724391, 1481682985, 2163791130, 13583590307, 5838404872, 12165330281, 28372578777, 7536755222

### 練習問題18.4(a)
# 鍵を生成します. 2つのなるべく大きな素数を入力してください：
# 1つ目：187963
# 2つ目：163841
# 指数k(30795694080と互いに素な数)：48611
# 暗号化は0, 復号化は1：1
# 復号化したい暗号(カンマ区切りでスペースなし)：5272281348, 21089283929, 3117723025, 26844144908, 22890519533, 26945939925, 27395704341, 2253724391, 1481682985, 2163791130, 13583590307, 5838404872, 12165330281, 28372578777, 7536755222
# MATHEMATICSISTHEQUEENOFSCIENCEANDNUMBERTHEORYISTHEQUEENOFMATHEMATICSKFGAUSS
