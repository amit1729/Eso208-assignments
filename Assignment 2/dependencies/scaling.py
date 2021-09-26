
def scale(mat,ts):
    mcpy = [i.copy() for i in mat]
    n = len(mat)
    for i in range(n):
        n1 = len(mcpy[i])
        max1 = abs(mcpy[i][0])
        for j in mcpy[i]:
            max1 = max(abs(j),max1)
        for j in range(n1):
            mcpy[i][j] = mcpy[i][j]/max1
    #print(mat)
    for i in range(n):
        temp = i
        max1 = mcpy[i][i]
        for j in range(i,n,1):
            if(abs(max1)<abs(mcpy[j][i])):
                temp = j
                max1 = mcpy[j][i]
        t = mat[i]
        mat[i] = mat[temp]
        mat[temp] = t
        t = mcpy[i]
        mcpy[i] = mcpy[temp]
        mcpy[temp] = t
    if(ts): return mcpy
    else: return mat

