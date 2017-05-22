# 基数の指定
# int()の第二引数に基数を指定すると基数に基づいた変換ができる

# 文字列から１６進数への変換
num1 = int("FF",16)
print(num1)

# 文字列から２進数への変換
num2 = int("1100",2)
print(num2)

# 数値を文字列に変換する
# str()のコンストラクタに数値を引数として渡すと数値型から文字列に変換する

str1 = str(1024)
print(str1)
print(type(str1))

# また、以下のように組み込み関数を使用するとそれぞれの基数の形式に沿った文字列に変換してくれる
# 16進数
str2 = hex(255)
print(str2)

# 8進数
str3 = oct(255)
print(str3)

# 2進数
str4 = bin(255)
print(str4)