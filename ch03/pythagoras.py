### 練習問題3.1(c)
# ピタゴラス数の表を出力する.

for v in range(1, 11):
    for u in range(1, 11):
        if v < u:
            print("v={:>2}, u={:>2}, a={:>4}, b={:>4}, c={:>4}".format(v, u, u*u - v*v, 2*u*v, u*u+v*v))

# 出力
# v= 1, u= 2, a=   3, b=   4, c=   5
# v= 1, u= 3, a=   8, b=   6, c=  10
# v= 1, u= 4, a=  15, b=   8, c=  17
# v= 1, u= 5, a=  24, b=  10, c=  26
# v= 1, u= 6, a=  35, b=  12, c=  37
# v= 1, u= 7, a=  48, b=  14, c=  50
# v= 1, u= 8, a=  63, b=  16, c=  65
# v= 1, u= 9, a=  80, b=  18, c=  82
# v= 1, u=10, a=  99, b=  20, c= 101
# v= 2, u= 3, a=   5, b=  12, c=  13
# v= 2, u= 4, a=  12, b=  16, c=  20
# v= 2, u= 5, a=  21, b=  20, c=  29
# v= 2, u= 6, a=  32, b=  24, c=  40
# v= 2, u= 7, a=  45, b=  28, c=  53
# v= 2, u= 8, a=  60, b=  32, c=  68
# v= 2, u= 9, a=  77, b=  36, c=  85
# v= 2, u=10, a=  96, b=  40, c= 104
# v= 3, u= 4, a=   7, b=  24, c=  25
# v= 3, u= 5, a=  16, b=  30, c=  34
# v= 3, u= 6, a=  27, b=  36, c=  45
# v= 3, u= 7, a=  40, b=  42, c=  58
# v= 3, u= 8, a=  55, b=  48, c=  73
# v= 3, u= 9, a=  72, b=  54, c=  90
# v= 3, u=10, a=  91, b=  60, c= 109
# v= 4, u= 5, a=   9, b=  40, c=  41
# v= 4, u= 6, a=  20, b=  48, c=  52
# v= 4, u= 7, a=  33, b=  56, c=  65
# v= 4, u= 8, a=  48, b=  64, c=  80
# v= 4, u= 9, a=  65, b=  72, c=  97
# v= 4, u=10, a=  84, b=  80, c= 116
# v= 5, u= 6, a=  11, b=  60, c=  61
# v= 5, u= 7, a=  24, b=  70, c=  74
# v= 5, u= 8, a=  39, b=  80, c=  89
# v= 5, u= 9, a=  56, b=  90, c= 106
# v= 5, u=10, a=  75, b= 100, c= 125
# v= 6, u= 7, a=  13, b=  84, c=  85
# v= 6, u= 8, a=  28, b=  96, c= 100
# v= 6, u= 9, a=  45, b= 108, c= 117
# v= 6, u=10, a=  64, b= 120, c= 136
# v= 7, u= 8, a=  15, b= 112, c= 113
# v= 7, u= 9, a=  32, b= 126, c= 130
# v= 7, u=10, a=  51, b= 140, c= 149
# v= 8, u= 9, a=  17, b= 144, c= 145
# v= 8, u=10, a=  36, b= 160, c= 164
# v= 9, u=10, a=  19, b= 180, c= 181



