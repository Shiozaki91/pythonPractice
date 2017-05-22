# 基礎的な関数の作り方を示す
# javaと違い戻り値の型を示すことはない点に注意


# 戻り値がない関数
# public void addNum1(int x, int y)みたいな
def addNum1(x,y):
    print(x + y)

addNum1(1,2)

# 戻り値が存在する場合
# public int addNum2(int x,int y)みたいな
def addNum2(x,y):
    ans = x + y
    return ans

ans = addNum2(2,3)
print(ans)
