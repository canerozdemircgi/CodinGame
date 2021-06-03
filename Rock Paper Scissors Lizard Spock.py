def Compare(player1, player2):
	if player1[1] == player2[1]:
		if int(player1[0]) < int(player2[0]):
			return player1
		else:
			return player2
	elif player1[1] == 'C' and player2[1] == 'P':
		return player1
	elif player1[1] == 'P' and player2[1] == 'R':
		return player1
	elif player1[1] == 'R' and player2[1] == 'L':
		return player1
	elif player1[1] == 'L' and player2[1] == 'S':
		return player1
	elif player1[1] == 'S' and player2[1] == 'C':
		return player1
	elif player1[1] == 'C' and player2[1] == 'L':
		return player1
	elif player1[1] == 'L' and player2[1] == 'P':
		return player1
	elif player1[1] == 'P' and player2[1] == 'S':
		return player1
	elif player1[1] == 'S' and player2[1] == 'R':
		return player1
	elif player1[1] == 'R' and player2[1] == 'C':
		return player1
	return player2

players = []
rounds = {}

n = int(input())
for i in range(n):
	player = input().split()
	players.append(player)
	rounds[player[0]] = []

while len(players) > 1:
	player1 = players.pop(0)
	player2 = players.pop(0)
	rounds[player1[0]].append(player2[0])
	rounds[player2[0]].append(player1[0])
	players.append(Compare(player1, player2))

winner = players[0][0]
print(winner)
print(' '.join(rounds[winner]))