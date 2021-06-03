n = int(input())
q = int(input())
fileTable = {}

for i in range(n):
	ext, mt = input().split()
	fileTable[ext.lower()] = mt

for i in range(q):
	fileName = input()
	if '.' in fileName:
		ext = fileName.rsplit('.', 1)[1].lower()
		if ext in fileTable:
			print(fileTable[ext])
		else:
			print('UNKNOWN')
	else:
		print('UNKNOWN')