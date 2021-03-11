# 產生一組隨機整數1~100
# 讓使用者重複猜
# 告知結果比答案大/小
# 答對的話終止程式，並印出答對了

import random
x = random.randint(1, 100)

a = input('猜一個從1~100的數字')
a = int(a)
while a != x:
	if a > x:
		print('再小一點')
	elif a < x:
		print('再大一點')
	a = input('猜一個從1~100的數字')
	a = int(a)
print('你答對了，答案是', x)
