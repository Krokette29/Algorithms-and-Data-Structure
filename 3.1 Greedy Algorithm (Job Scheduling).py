"""
1.Question 1
In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..

This file (jobs.txt) describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum).


2.Question 2
For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
"""

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
	