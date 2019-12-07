import random
import re


# Input Dict as a dictionary (without ** will Dict be changed outside the function)
def KargerMinCut(**dict):
    """
    Arguments:
    **dict -- the input dictionary of adjacent List

    Returns:
    numMinCut -- the number of Min Cut
    """
    numMinCut = 0

    # Loop until there are only two keys in Dict
    while len(dict) > 2:
        # Choose two connected vertices, this method is more efficient
        u_key = random.sample(list(dict), 1)[0]
        u = int(re.findall(r"\d+", u_key)[0])
        while True:
            v_flag = random.randint(0, len(dict[u_key]) - 1)
            v = dict[u_key][v_flag]
            v_key = "vertex " + str(v)
            if v != u:
                break

        # Replace v with u
        for i in dict.keys():
            dict[i] = [u if x == v else x for x in dict[i]]

        # Merge the two chosen vertices
        dict[u_key] += dict[v_key]
        dict.pop(v_key)  # dict.pop(key)

        # Remove self-loops
        for i_key in dict.keys():
            i = int(re.findall(r"\d+", i_key)[0])
            if dict[i_key].count(i) > 1:
                while True:
                    dict[i_key].remove(i)  # list.remove(value) ONLY ONCE!
                    if not (i in dict[i_key]):
                        break
                dict[i_key] = [i] + dict[i_key]

    # Calculate the number of Min Cut	
    for i in dict.keys():
        numMinCut += len(dict[i])
    numMinCut = (numMinCut - 2) / 2

    return int(numMinCut)


def main():
    adjDict = {}
    vertexFlag = 1
    ans = 0

    # Read the data line by line
    with open('data/kargerMinCut.txt', 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            adjDict["vertex " + str(vertexFlag)] = list(map(int, line.split()))
            vertexFlag += 1

    # Repeat n^2 times to get the optimal answer
    for i in range(len(adjDict) ^ 2):
        temp = KargerMinCut(**adjDict)
        if (temp < ans) or ans == 0:
            ans = temp

    print("The final result is: %i" % ans)


if __name__ == "__main__":
    main()
