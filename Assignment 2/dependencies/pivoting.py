
def pivot(mat):
    n = len(mat)
    for i in range(n):
        temp = i
        max1 = mat[i][i]
        for j in range(i,n,1):
            if(abs(max1)<abs(mat[j][i])):
                temp = j
                max1 = mat[j][i]
        t = mat[i]
        mat[i] = mat[temp]
        mat[temp] = t
    return mat
