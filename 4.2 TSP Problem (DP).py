"""
1.Question 1
In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.

tsp.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance sqrt{(x-z)^2 + (y-w)^2} between them.

In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here (http://www.math.uwaterloo.ca/tsp/world/countries.html). The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

HINT: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?
"""

from itertools import combinations
import math
INF = 2 ** 30

class City(object):
	def __init__(self, *coord):
		self.coord = coord


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numCities = int(data[0])
	cities = []
	for i in range(1, len(data)):
		cities.append(City(*map(float, data[i].split())))

	return numCities, cities


def calDistance(coord1, coord2):
	return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def listToBitmask(li):
	s = 0
	for item in li:
		s += 1 << item
	return s


def TSP_DP(numCities, cities):
	dp = {}
	dp[(1, 0)] = 0

	for m in range(2, numCities + 1):
		print("Now m = ", m)
		dpPrev = dp
		dp = {}

		for combine in combinations(range(1, numCities), m - 1):
			combine = list(combine)
			combine.insert(0, 0)
			bitmask = listToBitmask(combine)

			for j in combine[1:]:
				minValue = INF

				for k in combine:
					if k == j: continue
					distance = calDistance(cities[k].coord, cities[j].coord)
					oldBitmask = bitmask - (1 << j)
					oldValue = dpPrev.setdefault((oldBitmask, k), INF)
					value = oldValue + distance
					minValue = min([minValue, value, INF])
				dp[(bitmask, j)] = minValue

	bitmask = 2 ** numCities - 1
	minTotalValue = INF
	for j in range(1, numCities):
		distance = calDistance(cities[0].coord, cities[j].coord)
		value = dp[(bitmask, j)] + distance
		minTotalValue = min([minTotalValue, value, INF])
	
	return minTotalValue


def main():
	filePath = "data/tsp.txt"
	numCities, cities = dataReader(filePath)
	minTotalValue = TSP_DP(numCities, cities)
	print(int(minTotalValue))


if __name__ == "__main__":
	main()
