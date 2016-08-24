print("Please, enter number of elements in the array AL")
AL = [0] * int(input())
for inx in range(len(AL)):
    val = int(input())
    AL[inx] = val

print("Please, enter number of elements in the array AR")
AR = [0] * int(input())
for inx in range(len(AR)):
    val = int(input())
    AR[inx] = val
    
def merge(AL, AR):
    indx = 0
    inxL = 0
    inxR = 0
    B = [0] * (len(AL) + len(AR))
    for inx in range(len(AL) + len(AR)):
        if (inxL < len(AL)) or (inxR < len(AR)):
            if (inxR >= len(AR)) or (AL[inxL] < AR[inxR]):                
                B[indx] = AL[inxL]
                print(B[indx])
                inxL += 1
            elif (inxL >= len(AL)) or (AL[inxL] >= AR[inxR]):
                B[indx] = AR[inxR]
                print(B[indx])
                inxR += 1
            indx += 1
    print(B)

def mergeSort(A):
    if len(A) == 2:
        AL = A[0]
        AR = A[1]
        merge(AL, AR)
    lAL = 0
    rAR = len(A) - 1
    rAL = (rAR + lAL) // 2
    lAR = rAL + 1
    inxL = 0
    inxR = 0
    while (lAL < rAL):
        AL[inxL] = A[lAL]
        inxL += 1
        lAL += 1
    while (lAR < rAR):
        AR[inxR] = A[lAR]
        inxR += 1
        lAR += 1
        
    mergeSort(AL)
    mergeSort(AR)
    
merge(AL, AR)
