### 練習問題6.6(b)
# 3x+5yのリスト


for x in range(0, 11):
    for y in range(0, 11):
        print("x={:>2}, y={:>2}, 3x+5y={:>4}".format(x, y, 3*x+5*y))

# x= 0, y= 0, 3x+5y=   0
# x= 0, y= 1, 3x+5y=   5
# x= 0, y= 2, 3x+5y=  10
# x= 0, y= 3, 3x+5y=  15
# x= 0, y= 4, 3x+5y=  20
# x= 0, y= 5, 3x+5y=  25
# x= 0, y= 6, 3x+5y=  30
# x= 0, y= 7, 3x+5y=  35
# x= 0, y= 8, 3x+5y=  40
# x= 0, y= 9, 3x+5y=  45
# x= 0, y=10, 3x+5y=  50
# x= 1, y= 0, 3x+5y=   3
# x= 1, y= 1, 3x+5y=   8
# x= 1, y= 2, 3x+5y=  13
# x= 1, y= 3, 3x+5y=  18
# x= 1, y= 4, 3x+5y=  23
# x= 1, y= 5, 3x+5y=  28
# x= 1, y= 6, 3x+5y=  33
# x= 1, y= 7, 3x+5y=  38
# x= 1, y= 8, 3x+5y=  43
# x= 1, y= 9, 3x+5y=  48
# x= 1, y=10, 3x+5y=  53
# x= 2, y= 0, 3x+5y=   6
# x= 2, y= 1, 3x+5y=  11
# x= 2, y= 2, 3x+5y=  16
# x= 2, y= 3, 3x+5y=  21
# x= 2, y= 4, 3x+5y=  26
# x= 2, y= 5, 3x+5y=  31
# x= 2, y= 6, 3x+5y=  36
# x= 2, y= 7, 3x+5y=  41
# x= 2, y= 8, 3x+5y=  46
# x= 2, y= 9, 3x+5y=  51
# x= 2, y=10, 3x+5y=  56
# x= 3, y= 0, 3x+5y=   9
# x= 3, y= 1, 3x+5y=  14
# x= 3, y= 2, 3x+5y=  19
# x= 3, y= 3, 3x+5y=  24
# x= 3, y= 4, 3x+5y=  29
# x= 3, y= 5, 3x+5y=  34
# x= 3, y= 6, 3x+5y=  39
# x= 3, y= 7, 3x+5y=  44
# x= 3, y= 8, 3x+5y=  49
# x= 3, y= 9, 3x+5y=  54
# x= 3, y=10, 3x+5y=  59
# x= 4, y= 0, 3x+5y=  12
# x= 4, y= 1, 3x+5y=  17
# x= 4, y= 2, 3x+5y=  22
# x= 4, y= 3, 3x+5y=  27
# x= 4, y= 4, 3x+5y=  32
# x= 4, y= 5, 3x+5y=  37
# x= 4, y= 6, 3x+5y=  42
# x= 4, y= 7, 3x+5y=  47
# x= 4, y= 8, 3x+5y=  52
# x= 4, y= 9, 3x+5y=  57
# x= 4, y=10, 3x+5y=  62
# x= 5, y= 0, 3x+5y=  15
# x= 5, y= 1, 3x+5y=  20
# x= 5, y= 2, 3x+5y=  25
# x= 5, y= 3, 3x+5y=  30
# x= 5, y= 4, 3x+5y=  35
# x= 5, y= 5, 3x+5y=  40
# x= 5, y= 6, 3x+5y=  45
# x= 5, y= 7, 3x+5y=  50
# x= 5, y= 8, 3x+5y=  55
# x= 5, y= 9, 3x+5y=  60
# x= 5, y=10, 3x+5y=  65
# x= 6, y= 0, 3x+5y=  18
# x= 6, y= 1, 3x+5y=  23
# x= 6, y= 2, 3x+5y=  28
# x= 6, y= 3, 3x+5y=  33
# x= 6, y= 4, 3x+5y=  38
# x= 6, y= 5, 3x+5y=  43
# x= 6, y= 6, 3x+5y=  48
# x= 6, y= 7, 3x+5y=  53
# x= 6, y= 8, 3x+5y=  58
# x= 6, y= 9, 3x+5y=  63
# x= 6, y=10, 3x+5y=  68
# x= 7, y= 0, 3x+5y=  21
# x= 7, y= 1, 3x+5y=  26
# x= 7, y= 2, 3x+5y=  31
# x= 7, y= 3, 3x+5y=  36
# x= 7, y= 4, 3x+5y=  41
# x= 7, y= 5, 3x+5y=  46
# x= 7, y= 6, 3x+5y=  51
# x= 7, y= 7, 3x+5y=  56
# x= 7, y= 8, 3x+5y=  61
# x= 7, y= 9, 3x+5y=  66
# x= 7, y=10, 3x+5y=  71
# x= 8, y= 0, 3x+5y=  24
# x= 8, y= 1, 3x+5y=  29
# x= 8, y= 2, 3x+5y=  34
# x= 8, y= 3, 3x+5y=  39
# x= 8, y= 4, 3x+5y=  44
# x= 8, y= 5, 3x+5y=  49
# x= 8, y= 6, 3x+5y=  54
# x= 8, y= 7, 3x+5y=  59
# x= 8, y= 8, 3x+5y=  64
# x= 8, y= 9, 3x+5y=  69
# x= 8, y=10, 3x+5y=  74
# x= 9, y= 0, 3x+5y=  27
# x= 9, y= 1, 3x+5y=  32
# x= 9, y= 2, 3x+5y=  37
# x= 9, y= 3, 3x+5y=  42
# x= 9, y= 4, 3x+5y=  47
# x= 9, y= 5, 3x+5y=  52
# x= 9, y= 6, 3x+5y=  57
# x= 9, y= 7, 3x+5y=  62
# x= 9, y= 8, 3x+5y=  67
# x= 9, y= 9, 3x+5y=  72
# x= 9, y=10, 3x+5y=  77
# x=10, y= 0, 3x+5y=  30
# x=10, y= 1, 3x+5y=  35
# x=10, y= 2, 3x+5y=  40
# x=10, y= 3, 3x+5y=  45
# x=10, y= 4, 3x+5y=  50
# x=10, y= 5, 3x+5y=  55
# x=10, y= 6, 3x+5y=  60
# x=10, y= 7, 3x+5y=  65
# x=10, y= 8, 3x+5y=  70
# x=10, y= 9, 3x+5y=  75
# x=10, y=10, 3x+5y=  80



