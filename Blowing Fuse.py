import sys

n, m, c = [int(i) for i in input().split()]
nx = []
for i in input().split():
	nx.append([False, int(i)])

cx = cxMax = 0
for i in input().split():
	index = int(i) - 1
	if not nx[index][0]:
		cx += nx[index][1]
		if cx > c:
			print('Fuse was blown.')
			sys.exit(0)
		nx[index][0] = True
	else:
		cx -= nx[index][1]
		nx[index][0] = False
	cxMax = max(cxMax, cx)

print('Fuse was not blown.')
print('Maximal consumed current was {} A.'.format(cxMax))