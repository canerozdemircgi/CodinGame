import math

def CoordFloat(coord):
	return float(coord.replace(',' , '.'))

def CalculateDistance(long_b, long_a, lat_b, lat_a):
	x = (long_b - long_a) * math.cos((lat_a + lat_b) / 2.0)
	y = lat_b - lat_a
	return math.sqrt(x ** 2 + y ** 2) * 6371

lonUser = CoordFloat(input())
latUser = CoordFloat(input())
defibs = []
distances = []

n = int(input())
for i in range(n):
	defib = input().split(';')
	defibs.append(defib)
	distance = CalculateDistance(CoordFloat(defib[4]), lonUser, CoordFloat(defib[5]), latUser)
	distances.append(distance)

index = distances.index(min(distances))
print(defibs[index][1])