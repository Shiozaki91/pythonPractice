# モジュールからクラスを指定してインスタンスを生成する際はModule名.Class名が必要と言ったなあれは嘘だ
# 正確には、クラスを指定してimportする記法が存在する、よってそれを使用すれば一々Module名を指定する必要がなくなる
# 以下に    その例を示す

# calenderModuleからTextCalendarクラスのみをimportする
from calendar import TextCalendar

# fromでModule名とクラス名を指定してインポートしているのでインスタンス生成時に改めてModule名を指定する必要はない
cal = TextCalendar(6)
cal.prmonth(2017,5)

# !ただし、複数のモジュールからimportする場合や独自クラスを作成している場合はクラス名の重複に注意!
# クラス名の重複が起きた場合は、古いクラスから上書きされていく

# FIXME 月日を標準入力から指定することができるように書き換えること
import calendar
# import Calnedar.TextCalendar
