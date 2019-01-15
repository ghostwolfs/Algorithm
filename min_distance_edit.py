import numpy as np


# dynamic planning
def min_distance_edit(a, b):    
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    matrix = np.zeros((len(a)+1, len(b)+1))
    matrix = matrix.astype(np.int16)
    for index in range(len(a)+1):
        matrix[index][0] = index
    for index in range(len(b)+1):
        matrix[0][index] = index

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                case1 = matrix[i-1][j] + 1
                case2 = matrix[i][j-1] + 1
                case3 = matrix[i-1][j-1] + 1
                matrix[i][j] = min(case1, case2, case3) 
    return matrix[len(a)][len(b)]


# recursive
def min_distance_edit(a, b, lenA, lenB):
    if lenA == 0:
        return lenB
    if lenB == 0:
        return lenA
    
    if a[lenA-1] == b[lenB-1]:
        return min_distance_edit(a, b, lenA-1, lenB-1)
    else:
        case1 = min_distance_edit(a, b, lenA-1, lenB) + 1
        case2 = min_distance_edit(a, b, lenA, lenB-1) + 1
        case3 = min_distance_edit(a, b, lenA-1, lenB-1) + 1
        return min(case1, case2, case3)