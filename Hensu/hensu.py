# 変数名の付け方
# 使える文字：半角abcと数字、あとはアンダースコア
# ただし、最初の一文字に数字は使えない
# OK: name number String Integer_number Number1 Number2 _Goukei
# NG: 1Fuji 2Taka 3Nasubi ?Color #Twitter /Alphabed

# 基礎的な変数の使い方
# javaみたいに変数の型を宣言することはない

name = "kazuya"

# 型を調べる関数
print(type(name))
print("name:" + name)

# javaみたいに変数同士の計算もできる
# とはいえ文字列と数字の扱いは違うらしく,がないとコンパイルエラー(コンパイルじゃないけど)
num1 = 1
num2 = 2
print("sum = " , num1 + num2)

# 変数と数値型も可能
print(num1 + 1)

# みんな大好き代入演算子も使える
num3 = 0
num3 += num1

print(++num3)

# ただし、++ -- は使えないことに注意

# ある値に対して複数の変数名が用意できる
# 詳しく書くとメモリに格納された値に対して参照する変数がいくつあってもいいってこと

name1 = "takahashi"
name2 = name1

print(name1)
print(name2)

# 演習
# 身長180cmの人間の標準体重を求めるプログラムを作成せよ
# 標準体重を求める式は以下の通りとする
# 標準体重 = bmi * 身長(m)^2
# ただし、bmiは２２とする
