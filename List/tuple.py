# タプル：イミュータブルな配列
# ※イミュータブル：要素が変更不可である配列、要素を一度初期化してしまえば以降その要素は変更できない

# タプルの生成例
# !配列の際は[]で初期化していたがタプルの場合は()で初期化している点に注意!
nameTuple = ("takashi","kenta","hiroaki")

# 配列と同様に変数名を指定すると中身を全部吐き出してくれる
print(nameTuple)

# 配列と同様に要素の指定を行うことができる
# !要素の指定を行う際は[]を使用することに注意!
print(nameTuple[0])

# ただし、タプルはイミュータブルなので要素を指定して後から値を代入することはできない
# 以下はエラーとなる例
# nameTuple[0] = "NEET"

# Listとtupleは相互に変換ができる
# listクラスのコンストラクタにタプルを引数で渡すとListに変換された物が返ってくる
nameList = list(nameTuple)

#List(ミュータブル)なので要素に対して代入が可能
nameList[0] = "NEET"
print(nameList)

# 同様にtupleクラスのコンストラクタに引数としてListを渡すとtupleに変換したものが返ってくる
nameTuple = tuple(nameList)
# tuple(イミュータブル)なので以下のように要素を指定しての代入は不可能
# nameTuple[0] = "takashi"
