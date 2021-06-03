sudoku = [[0] * 9 for i in range(9)]
for i in range(9):
	sudoku[i] = input().split()
	if len(set(sudoku[i])) != 9:
		print('false')
		exit(0)

for j in range(9):
	row = [i[j] for i in sudoku]
	if len(set(row)) != 9:
		print('false')
		exit(0)

sub = [[[] for j in range(3)] for i in range(3)]
for i in range(9):
	for j in range(9):
		sub[int(i / 3)][int(j / 3)].append(sudoku[i][j])
for i in range(3):
	for j in range(3):
		if len(set(sub[i][j])) != 9:
			print('false')
			exit(0)
print('true')