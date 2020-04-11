"""
1.Question 1
In this assignment we will revisit an old friend, the traveling salesman problem (TSP). This week you will implement a heuristic for the TSP, rather than an exact algorithm, and as a result will be able to handle much larger problem sizes. Here is a data file describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).

nn.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance sqrt{(x-z)^2 + (y-w)^2} between them.

You should implement the nearest neighbor heuristic:

Start the tour at the first city.
Repeatedly visit the closest city that the tour hasn't visited yet. In case of a tie, go to the closest city with the lowest index. For example, if both the third and fifth cities have the same distance from the first city (and are closer than any other city), then the tour should begin by going from the first city to the third city.
Once every city has been visited exactly once, return to the first city to complete the tour.
In the box below, enter the cost of the traveling salesman tour computed by the nearest neighbor heuristic for this instance, rounded down to the nearest integer.

[Hint: when constructing the tour, you might find it simpler to work with squared Euclidean distances (i.e., the formula above but without the square root) than Euclidean distances. But don't forget to report the length of the tour in terms of standard Euclidean distance.]
"""

import math
class City(object):
	def __init__(self, *coord):
		self.coord = coord


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numCities = int(data[0])
	cities = []
	for i in range(1, len(data)):
		dataList = data[i].split()
		ID = int(dataList[0])
		x, y = map(float, dataList[1:])
		cities.append(City(x, y))

	return numCities, cities


def calSqaureDistance(coord1, coord2):
	return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2


def TSP_approx(numCities, cities):
	start = cities[0]
	totalDistance = 0
	prev = cities[0]
	del cities[0]
	while cities:
		if len(cities) % 100 == 0: print(len(cities))
		minSqaureDistance = None
		minCityIndex = None
		minCity = None
		for k, v in enumerate(cities):
			sqaureDistance = calSqaureDistance(prev.coord, v.coord)
			if minSqaureDistance != None and sqaureDistance < minSqaureDistance or minSqaureDistance == None:
				minSqaureDistance = sqaureDistance
				minCityIndex, minCity = k, v
		prev = minCity
		del cities[minCityIndex]
		totalDistance += math.sqrt(minSqaureDistance)

	totalDistance += math.sqrt(calSqaureDistance(prev.coord, start.coord))
	return totalDistance


def main():
	filePath = "data/tsp_nn.txt"
	numCities, cities = dataReader(filePath)
	totalDistance = TSP_approx(numCities, cities)
	print(int(totalDistance))


if __name__ == "__main__":
	main()
