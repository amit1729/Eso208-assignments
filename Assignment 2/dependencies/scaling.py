
def scale(mat):
    mcpy = [i.copy() for i in mat]
    n = len(mat)
    for i in range(n):
        n1 = len(mcpy[i])
        max1 = abs(mcpy[i][0])
        for j in mcpy[i]:
            max1 = max(abs(j),max1)
        for j in range(n1):
            mcpy[i][j] = mcpy[i][j]/max1
    return mcpy

"""def pivot(mat,ts,column):
    mcpy = [i.copy() for i in mat]
    n = len(mat)
    #print(mat)
    temp = column
    max1 = mcpy[column][column]
    for j in range(column,n,1):
        if(abs(max1)<abs(mcpy[j][column])):
            temp = j
            max1 = mcpy[j][column]
    t = mat[column]
    mat[column] = mat[temp]
    mat[temp] = t
    t = mcpy[column]
    mcpy[column] = mcpy[temp]
    mcpy[temp] = t
    if(ts): return mcpy, temp
    else: return mat, temp"""

