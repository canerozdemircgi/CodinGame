from enum import Enum

class Operations(Enum):
	ENCODE = 0
	DECODE = 1

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def OperationShift(operation, text, number):
	result = []
	if operation == Operations.ENCODE:
		for i in range(len(text)):
			result.append(alphabet[(alphabet.find(text[i]) + number) % len(alphabet)])
			number = (number + 1) % len(alphabet)
	elif operation == Operations.DECODE:
		for i in range(len(text)):
			result.append(alphabet[(alphabet.find(text[i]) - number) % len(alphabet)])
			number = (number + 1) % len(alphabet)
	return ''.join(result)

def OperationRotor(operation, text, rotor):
	result = []
	if operation == Operations.ENCODE:
		for i in range(len(text)):
			result.append(rotor[alphabet.find(text[i])])
	elif operation == Operations.DECODE:
		for i in range(len(text)):
			result.append(alphabet[rotor.find(text[i])])
	return ''.join(result)

operation = input()
number = int(input())
rotor = [input() for i in range(3)]
text = input()

if Operations[operation] == Operations.ENCODE:
	text = OperationShift(Operations.ENCODE, text, number)
	text = OperationRotor(Operations.ENCODE, text, rotor[0])
	text = OperationRotor(Operations.ENCODE, text, rotor[1])
	text = OperationRotor(Operations.ENCODE, text, rotor[2])
elif Operations[operation] == Operations.DECODE:
	text = OperationRotor(Operations.DECODE, text, rotor[2])
	text = OperationRotor(Operations.DECODE, text, rotor[1])
	text = OperationRotor(Operations.DECODE, text, rotor[0])
	text = OperationShift(Operations.DECODE, text, number)

print(text)