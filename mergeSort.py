print("Please, enter number of elements in the array")
A = [0] * int(input())
for inx in range(len(A)):
    val = int(input())
    A[inx] = val


def merge(A):
    l = 0
    r = len(A) - 1
    lm = (l + r)//2
    rm = lm + 1
    indx = 0
    inxL = 0
    inxR = lm + 1
    print("//////", len(A))
    B = [0] * len(A)
    for inx in range(len(A)):
        if (inxL <= lm) or (inxR <= r):
            if (inxR > r) or (A[inxL] < A[inxR]):                
                B[indx] = A[inxL]
                print(B[indx])
                inxL += 1
            elif (inxL > lm) or (A[inxL] >= A[inxR]):
                B[indx] = A[inxR]
                print(B[indx])
                inxR += 1
            indx += 1
    print(B)
        
merge(A)
