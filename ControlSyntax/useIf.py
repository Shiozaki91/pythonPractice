# pythonにおけるif文の使い方を示す
# 書き方としてjavaとは違う点があるでの注意
# FIXME 入力できる環境を考えること、コマンドラインから実行する？

inputNumber = int(input())

# if 条件式:
if inputNumber >= 100:
    # pythonではブロックを作る際に{}を使わず半角スペースで表現する
    # 半角スペース4つ下げでブロックを表現するのでtabの設定を半角スペース4つにしておくと便利
    print("入力された数字は100以上です")
# javaで言うとelseif
# 基本的にはifと書式は変わらない
elif inputNumber < 100 & 50 <= inputNumber:
    print("入力された数字は５０以上100未満です")
# else、当然だけど条件式はない
# でもコロンは必要
else:
    print("入力された数字は50未満です")

# pass
# を使用することで何もしないと言う選択肢がとれる
