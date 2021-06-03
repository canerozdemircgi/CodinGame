caches = {}
for i in range(int(input())):
	x = input()
	y = x
	while True:
		y = sum([int(r) * int(r) for r in str(y)])
		if y == 1:
			print(str(x) + ' :)')
			break
		if y in caches:
			print(str(x) + ' :(')
			break
		caches[y] = False
	caches = {}