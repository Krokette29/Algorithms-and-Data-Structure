# def DFS(G, s):
#     # TODO
#
# def computeSCC():
#     # TODO


def main():
    adjDict = {}

    # Read the data line by line
    with open('data/SCC.txt', 'r') as f:
        while True:
            line = f.readline().strip()  # output every line as a string, striping line breaks
            if not line:
                break

            lineList = list(map(int, line.split()))  # split line string, make every element to int type, make a list

            if ("vertex " + str(lineList[0])) in adjDict.keys():
                adjDict["vertex " + str(lineList[0])].append(lineList[1])
            else:
                adjDict["vertex " + str(lineList[0])] = [lineList[1]]

    print(adjDict["vertex 1"])


if __name__ == "__main__":
    main()
