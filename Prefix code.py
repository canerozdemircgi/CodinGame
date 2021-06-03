n = int(input())
bMax = 0
bc = {}
for i in range(n):
	inputs = input().split()
	bc[inputs[0]] = chr(int(inputs[1]))
	bMax = max(bMax, len(inputs[0]))

s = input()
i = 0
j = 1
result = ''

while i < len(s):
	if s[i : i + j] in bc:
		result += bc[s[i : i + j]]
		i += j
		j = 1
	else:
		j += 1
		if j - 1 > bMax:
			print('DECODE FAIL AT INDEX {}'.format(i))
			exit(0)

print(result)