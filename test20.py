#randomモジュールのrandint関数を読み込む
from random import randint
point=randint(0,100)#0~100の乱数
#判定
if point >=80 :
    result="gクラス"
elif point>=60:
    result="Bクラス"
elif point>=30:
    result="Cクラス"
else :
    result="不合格"
print(f"{point}点:{result}")
