# 產生一組隨機整數1~100
# 讓使用者重複猜
# 告知結果比答案大/小
# 答對的話終止程式，並印出答對了
# 印出答了幾次，讓使用者自己輸入起始和結束值

import random
start = input('請輸入起始值:')
end = input('請輸入結束值:')
start = int(start)
end = int(end)
x = random.randint(start, end)
count = 0
print('請從', start, '~', end,'間猜一個數字')

while True:
	count += 1 # count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == x:
		print('恭喜你答對了!答案是', x, '!')
		break
	elif num > x:
		print('再猜小一點')
	elif num < x:
		print('再猜大一點')
	print('你已經猜了', count, '次')