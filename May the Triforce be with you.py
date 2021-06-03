n = int(input())
xn = (n * 4) - 1
yn = n * 2
matrix = [[' '] * yn for i in range(xn)]

i = 0
for y in range(int(yn / 2)):
	for x in range(xn):
		if xn / 2 - i - 1 < x < xn / 2 + i:
			matrix[x][y] = '*'
	i += 1
i = 0
for y in range(int(yn / 2), yn):
	for x in range(xn):
		if xn / 2 - i - 1 < x < xn / 2 + i:
			matrix[x - n][y] = '*'
			matrix[x + n][y] = '*'
	i += 1

matrix[0][0] = '.'
result = []
for y in range(yn):
	tmp = []
	for x in range(xn):
		tmp.append(matrix[x][y])
	result.append(''.join(tmp).rstrip())
print('\n'.join(result))