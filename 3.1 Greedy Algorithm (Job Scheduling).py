class Job(object):
	def __init__(self, weight, length):
		self.weight = weight
		self.length = length
		self.difference = weight - length
		self.ratio = weight / length


def dataReader(filePath):
	jobs = []
	numJobs = None

	with open(filePath) as f:
		data = f.readlines()

	for index, item in enumerate(data):
		if index == 0:
			numJobs = int(item)
		else:
			values = list(map(int, item.split()))
			jobs.append(Job(values[0], values[1]))

	return numJobs, jobs


def scheduler(jobs, method):
	if method == "difference":
		jobSequence = list(sorted(jobs, key=lambda item:(item.difference, item.weight), reverse=True))

	elif method == "ratio":
		jobSequence = list(sorted(jobs, key=lambda item:item.ratio, reverse=True))

	else:
		raise ValueError("No such method!")

	return jobSequence


def calculateWeightedCompletionTime(jobSequence):
	time = 0
	totalTime = 0
	for job in jobSequence:
		time += job.length
		totalTime += time * job.weight

	return totalTime


def main():
	filePath = "data/jobs.txt"
	numJobs, jobs = dataReader(filePath)
	jobSequenceDifference = scheduler(jobs, "difference")
	jobSequenceRatio = scheduler(jobs, "ratio")
	totalTimeDifference = calculateWeightedCompletionTime(jobSequenceDifference)
	totalTimeRatio = calculateWeightedCompletionTime(jobSequenceRatio)
	print("Total completion time with difference: \t", totalTimeDifference)
	print("Total completion time with ratio: \t\t", totalTimeRatio)


if __name__ == "__main__":
	main()
	