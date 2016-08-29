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

def ifSortCheck(A):
    for inx in range(len(A) - 2):
        if (A[inx] > A[inx+1]):
            return False
    
    return True

def mergeSort(*args):

    if len(args) < 1:
        return []
    else:
        A = args[0]
        

    if len(args) < 2:
        l = 0
    else:
        l = args[1]
        
    
    if len(args) < 3:
        r = len(A) - 1
    else:
        r = args[2]       


    m = int((l+r)//2)
    
    if l < m:
        mergeSort(A, l, m)
        
    if m+1 < r:
        mergeSort(A, m+1, r)
        
    merge(A, l, r)

    return A


if __name__ == '__main__':
            
    if (ifSortCheck(mergeSort([5, 9, 3, 2, 4, 15, 0])) == False):        
        print("mergeSort doesn't work")
    if (ifSortCheck(mergeSort([7, 9, 3, 5])) == False):
        print("mergeSort doesn't work")



