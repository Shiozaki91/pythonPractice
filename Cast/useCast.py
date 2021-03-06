# floatクラスのインスタンスを生成するにあたってコンストラクタに"文字列"を引数として渡している
num = float("3.14")

# 浮動小数型の変数numをコンソールに出力　
print(num)

# type()クラスのインスタンスに引数を渡せば引数の型を返してくれる
# これによりnumの型がfloatに変わっていることが分かる
print(type(num))

# floatに整数の文字列を渡しても同様である
num2 = float("15")
print(num2)
print(type(num2))

# floatのコンストラクタに数値変換できない文字列を渡すと当然エラーとなる
# 以下エラーとなる例(コンパイルできなくなるのでコメントアウトしておく,外して試してみること)
# num3 = float("abc")

# 整数に変換したければ同様にint()を使用すること
