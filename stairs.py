# [RG]: Please, make it as a function with arguments
# [RG]: Please, leave a comments before each logic block, ie each loop and condition

print("Please, enter the number of steps of the staircase")
resultArr = [0] * int(input())
print(len(resultArr))

for inx in range(len(resultArr)):
	resultArr[inx] = 0 # [GR] Indentation is not consistent with lines 12-14 for example

print("Please, enter count of possible values of number of steps in the jumps in ascending order")
jumps = [0] * int(input())
for inx in range(len(jumps)):
    val = int(input())
    jumps[inx] = val

print(len(jumps))

print("Len of the resultArr is ", len(resultArr))

for inx in range(len(resultArr)):
    for jumpsInx in range(len(jumps)):
        if (inx == jumps[jumpsInx]):
            resultArr[inx] += 1
        if (inx > jumps[jumpsInx]):
            if (resultArr[inx - jumps[jumpsInx]] != 0):
                resultArr[inx] += resultArr[inx - jumps[jumpsInx]]

print("There are ", resultArr[len(resultArr)-1], " variants of the ways to aproach the step .", len(resultArr))

# [RG] :
if __name__ == '__main__':
	# [RG] Here please call function several times as a test with corner cases please
	pass
