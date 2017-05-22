# 乱数を使用する際に使われるrandomモジュールの使い方を示す
# randomモジュールをインポートする
import random

# randint(a,b)はaからbの範囲でランダムなint型の値を生成する
print(random.randint(1,10))

# randrange(a)は０から「a未満」の範囲で値を生成する
print(random.randrange(10))
