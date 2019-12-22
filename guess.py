# 產生一個隨機整數1~100 (不要印出)
#讓使用者重複數字去猜
#猜對的話印出 "終於猜對了"
#猜錯的話印出, 要告訴他比答案大/小


import random

r = random.randint(1, 100	)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')

