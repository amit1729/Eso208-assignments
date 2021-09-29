
def pivot(matrix,i):
    mat = [i.copy() for i in matrix]
    n = len(mat)
    temp = i
    max1 = mat[i][i]
    for j in range(i,n,1):
        if(abs(max1)<abs(mat[j][i])):
            temp = j
            max1 = mat[j][i]
    mat[i], mat[temp] = mat[temp], mat[i]
    return mat,temp
