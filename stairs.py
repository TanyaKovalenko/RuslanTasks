numOfStairs = [7, 8, 0, 15, 4]
numOfSteps = [[2, 3, 4], [5, 2], [], [5, 4, 3], [1]]
                
def findNumOfWays(numOfStairs, numOfSteps):
        for numOfStairsInx in range(len(numOfStairs)):
                if (numOfStairs[numOfStairsInx] == 0):
                        print("There are 0 variants of the ways to aproach the step .0")
                elif (numOfStairs[numOfStairsInx] == 1):
                        print("There are 0 variants of the ways to aproach the step .1")
                else:
                        resultArr = [0] * numOfStairs[numOfStairsInx]
                        for inx in range(len(resultArr)):
                                resultArr[inx] = 0
                        for inx in range(len(resultArr)):
                                jumps = numOfSteps[numOfStairsInx]
                                for jumpsInx in range(len(jumps)):
                                        if (inx == jumps[jumpsInx]):
                                                resultArr[inx] += 1
                                        if (inx > jumps[jumpsInx]):
                                                if (resultArr[inx - jumps[jumpsInx]] != 0):
                                                        resultArr[inx] += resultArr[inx - jumps[jumpsInx]]
                        print("There are ", resultArr[len(resultArr)-1], " variants of the ways to aproach the step .", len(resultArr))
        

if __name__ == '__main__':
        findNumOfWays(numOfStairs, numOfSteps)
        pass
