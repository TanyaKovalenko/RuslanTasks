def findNumOfWays(numOfStairs, jumps):
        if (numOfStairs == 0):
                print("There are 0 variants of the ways to aproach the step .0")
        elif (numOfStairs == 1):
                print("There are 0 variants of the ways to aproach the step .1")
        else:
                resultArr = [0] * numOfStairs
                for inx in range(len(resultArr)):
                        resultArr[inx] = 0
                for inx in range(len(resultArr)):                               
                        for jumpsInx in range(len(jumps)):
                                if (inx == jumps[jumpsInx]):
                                        resultArr[inx] += 1
                                if (inx > jumps[jumpsInx]):
                                        if (resultArr[inx - jumps[jumpsInx]] != 0):
                                                resultArr[inx] += resultArr[inx - jumps[jumpsInx]]
                print("There are ", resultArr[len(resultArr)-1], " variants of the ways to aproach the step .", len(resultArr))
        

if __name__ == '__main__':
        findNumOfWays(7, [2, 3, 4])
        findNumOfWays(8, [5, 2])
        findNumOfWays(0, [])
        findNumOfWays(15, [5, 4, 3])
        findNumOfWays(4, [1])
        pass
