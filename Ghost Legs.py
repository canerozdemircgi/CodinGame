w, h = [int(i) for i in input().split()]
matrix = [[''] * w for i in range(h)]

for j in range(h):
	line = input()
	for i in range(len(line)):
		matrix[j][i] = line[i]

for i in range(0, w, 3):
	result = [matrix[0][i]]
	for j in range(1, h - 1):
		if i - 1 >= 0 and '-' == matrix[j][i - 1]:
			i -= 3
		elif i + 1 < w and '-' == matrix[j][i + 1]:
			i += 3
	result.append(matrix[h - 1][i])
	print(''.join(result))