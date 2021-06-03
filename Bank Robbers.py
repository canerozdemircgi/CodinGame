import math

class Chunk:
	size = 0
	sizeMax = 0
	data = []

	def __init__(self, size_max):
		self.sizeMax = size_max
		self.data = [0] * size_max

	def take(self, element):
		if self.size < self.sizeMax:
			self.data[self.size] = element
			self.size += 1
			return 0
		else:
			element_min = min(self.data)
			self.data.remove(element_min)
			self.data = [element - element_min for element in self.data]
			self.data.append(element)
			return element_min

	def give(self):
		return max(self.data)

r = int(input())
v = int(input())
work = []
for i in range(v):
	c, n = [int(j) for j in input().split()]
	work.append(math.pow(10, n) * math.pow(5, c - n))

chunk = Chunk(r)
result = 0
for i in range(0, v):
	result += chunk.take(work[i])
result += chunk.give()
print(int(result))