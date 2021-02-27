country = input('請問你是哪國人： ')
age = input('請輸入你的年齡： ')
age = int(age)

if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('還不能考喔，再等', 18-age,'年吧')

elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('還不能考喔，再等', 16-age, '年吧')

else:
	print('你只能輸入台灣或美國喔')