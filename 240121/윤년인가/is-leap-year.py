# 변수 선언, 입력
y = int(input())

# 출력
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
	print("true")
else:
	print("false")