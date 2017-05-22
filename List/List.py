# Javaでいう配列型
# Javaのように変数名の後に配列を示す[]を使用する必要はない

nameList = ["takashi","kenta","hiroaki"]

#また、中身を出力する際は変数名を指定すれば勝手に中身を全部吐いてくれる
print(nameList)

# また、Javaのように要素を指定して出力も可能
print(nameList[0])

# 同様に要素を指定しての出力も可能
nameList[0] = "NEET"
print(nameList[0])

# Javaでいうlength()に当たる組み込み関数
print(len(nameList))
