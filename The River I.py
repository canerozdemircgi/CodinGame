r1 = int(input())
r2 = int(input())

while True:
	if r1 > r2:
		r2 += sum([int(r) for r in str(r2)])
	elif r2 > r1:
		r1 += sum([int(r) for r in str(r1)])
	if r1 == r2:
		break

print(r1)