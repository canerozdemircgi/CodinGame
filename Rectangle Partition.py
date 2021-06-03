xs = [0]
ys = [0]
w, h, count_x, count_y = [int(i) for i in input().split()]
for i in input().split():
	xs.append(int(i))
xs.append(w)
for i in input().split():
	ys.append(int(i))
ys.append(h)

dictX = {}
for x1 in range(len(xs)):
	for x2 in range(x1 + 1, len(xs)):
		if xs[x2] - xs[x1] in dictX:
			dictX[xs[x2] - xs[x1]] += 1
		else:
			dictX[xs[x2] - xs[x1]] = 1

count = 0
for y1 in range(len(ys)):
	for y2 in range(y1 + 1, len(ys)):
		if ys[y2] - ys[y1] in dictX:
			count += dictX[ys[y2] - ys[y1]]

print(count)