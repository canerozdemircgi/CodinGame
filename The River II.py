param = int(input())
for i in range(max(1, param - len(str(param)) * 9), param - 1):
	while True:
		i += sum([int(r) for r in str(i)])
		if i < param:
			continue
		if i == param:
			print('YES')
			exit(0)
		elif i > param:
			break
print('NO')