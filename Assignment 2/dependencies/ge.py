import pivoting, scaling, substitutions

def ge(mat,pivot = False,scale = False,LU_decompose = False):
    n = len(mat)
    b = [i[n] for i in mat]
    if(pivot): mat = pivoting.pivot(mat)
    print(mat)
    if(scale): mat = scaling.scale(mat)
    print(mat)
    x = [0]*n
    l = [[0]*n for i in range(n)]
    for i in range(n):
        l[i][i] = 1
    
    #Forward-Elimination
    for i in range(n-1):
        for j in range(i+1,n,1):
            l[j][i] = mat[j][i]/mat[i][i]
            for k in range(n+1):
                mat[j][k] = mat[j][k] - l[j][i]*mat[i][k]

    #Back-Substitution
    if(not LU_decompose):
        x = substitutions.back_substitution(mat)
        print(x)
    
    else:
        #Forward-substitution
        y = [0]*n
        for i in range(n):
            l[i].append(b[i])
        
        y = substitutions.forward_substitution(l)

        for i in range(n):
            mat[i][n] = y[i]

        #Back-substitution
        x = substitutions.back_substitution(mat)
        print(x)

        
mat = [[1,1,1,7],[1,2,2,13],[1,3,1,13]]
ge(mat,pivot=True,LU_decompose=True)
