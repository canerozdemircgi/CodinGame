from queue import LifoQueue

expression = input()
stack = LifoQueue(maxsize = len(expression))
for character in expression:
	if character in ('{', '[', '('):
		stack.put(character)
	elif '}' == character:
		if stack.empty() or '{' != stack.get():
			print('false')
			exit(0)
	elif ']' == character:
		if stack.empty() or '[' != stack.get():
			print('false')
			exit(0)
	elif ')' == character:
		if stack.empty() or '(' != stack.get():
			print('false')
			exit(0)
print(str(stack.empty()).lower())