import sys
import math

width, height = [int(i) for i in input().split()]
matrix = [[0] * width for i in range(height)]
for i in range(height):
	matrix[i] = list(input())

for i in range(height):
	for j in range(width):
		if matrix[i][j] == '#':
			continue
		count = 0
		if i - 1 >= 0:
			if matrix[i - 1][j] != '#':
				count += 1
		if i + 1 < height:
			if matrix[i + 1][j] != '#':
				count += 1
		if j - 1 >= 0:
			if matrix[i][j - 1] != '#':
				count += 1
		if j + 1 < width:
			if matrix[i][j + 1] != '#':
				count += 1
		matrix[i][j] = str(count)

for i in range(height):
		print(''.join(matrix[i]))