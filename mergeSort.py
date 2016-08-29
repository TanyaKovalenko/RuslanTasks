import copy

def merge(A, l, r):
    
    m = int((l+r) // 2)
    inxL = l
    inxR = m + 1
    inx = l
    B = copy.deepcopy(A)

    while (inxL <= m) and (inxR <= r):
        
        if A[inxL] < A[inxR]:
            B[inx] = A[inxL]        
            inxL += 1
        else:
            B[inx] = A[inxR]      
            inxR += 1
            
        inx += 1
        
    while inxL <= m:
        B[inx] = A[inxL]
        inxL += 1
        inx += 1
        
    while inxR <= r:
        B[inx] = A[inxR]
        inxR += 1
        inx += 1

    for indx in range(len(A)):
        A[indx] = B[indx]

def mergeSort(A, l, r):
    
    m = int((l+r)//2)
    
    if l < m:
        mergeSort(A, l, m)
        
    if m+1 < r:
        mergeSort(A, m+1, r)
        
    merge(A, l, r)

    return A


if __name__ == '__main__':
        assert mergeSort([5, 9, 3, 2, 4, 15, 0], 0, 6) == [0, 2, 3, 4, 5, 9, 15]
        assert mergeSort([7, 9, 3, 5], 0, 3) == [3, 5, 7, 9]



