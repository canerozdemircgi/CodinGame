n = int(input())
l = int(input())

map_n = [[0] * n for i in range(n)]

for i in range(n):
	j = 0
	for cell in input().split():
		if cell == 'C':
			for x in range(-1 * l, l):
				for y in range(-1 * l, l):
					if 0 <= i + x < n and 0 <= j + y < n:
						map_n[i + x][j + y] += l - max(abs(x), abs(y))
		j += 1

count = 0
for x in range(n):
	for y in range(n):
		if map_n[x][y] == 0:
			count += 1
print(count)