ones = [len(x) for x in input().split('0')]
ones_pool = [0] * (len(ones) - 1)
for i in range(0, len(ones_pool)):
	ones_pool[i] = ones[i] + ones[i + 1]
ones_pool.sort(reverse=True)
print(ones_pool[0] + 1)