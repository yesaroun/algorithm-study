# 직각 삼각형의 넓이를 구하는 함수
def triangle(height, base):
	return height * base / 2

if __name__ == "__main__":
	print(triangle(1, 2) == 1)