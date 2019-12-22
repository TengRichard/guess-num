# 產生一個隨機整數1~100 (不要印出)
#讓使用者重複數字去猜
#猜對的話印出 "終於猜對了"
#猜錯的話印出, 要告訴他比答案大/小


import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
count = 0
r = random.randint(start, end)
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')

