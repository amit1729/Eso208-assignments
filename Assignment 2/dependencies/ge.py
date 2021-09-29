from dependencies import pivoting, scaling, substitutions

def ge(mat,pivot = False,scale = False,ts = False,LU_decompose = False):
    n = len(mat) 
    x = [0]*n
    l = [[0]*n for i in range(n)]
    for i in range(n):
        l[i][i] = 1
    
    mcpy  = [i.copy() for i in mat]
    _  = [i.copy() for i in mat]
    if(ts):
        mcpy = scaling.scale(mcpy)
        mat = scaling.scale(mat)
    if(scale and (not ts)):
        _ = scaling.scale(mat)
    b = [i[n] for i in mat]

    #Forward-Elimination
    for i in range(n-1):
        if(pivot or ts):
            mat, row = pivoting.pivot(mat,i)
            mcpy[row], mcpy[i] = mcpy[i], mcpy[row]
            b[row], b[i] = b[i], b[row]
            for q in range(i):
                l[i][q], l[row][q] = l[row][q], l[i][q]
        if(scale and (not ts)):
            _, row = pivoting.pivot(_,i)
            mat[i], mat[row] = mat[row], mat[i]
            mcpy[row], mcpy[i] = mcpy[i], mcpy[row]
            b[row], b[i] = b[i], b[row]
        
        for j in range(i+1,n,1):
            l[j][i] = mat[j][i]/mat[i][i]
            t = _[j][i]/_[i][i]
            for k in range(n+1):
                mat[j][k] = mat[j][k] - l[j][i]*mat[i][k]
                _[j][k] = _[j][k] - t*_[i][k]
    #print(mat)
    if(pivot or scale):
        with open("outputs/outputs.txt",'w') as f:
            f.write("\n")
            f.write("Scaled/Pivoted Matrix:")
            f.write("\n")
            for i in range(n):
                f.write(", ".join([str(j) for j in mcpy[i]]))
                f.write('\n')
    else:
        with open("outputs/outputs.txt",'w') as f:
            f.write("")    

    
    #Back-Substitution
    if(not LU_decompose):
        x = substitutions.back_substitution(mat)
        with open("outputs/outputs.txt",'a') as f:
            f.write("\n")
            f.write("X: ")
            f.write("\n")
            f.write("\n".join([str(j) for j in x]))
    
    else:
        with open("outputs/outputs.txt",'a') as f:
            f.write("\n")
            f.write("L: ")
            f.write("\n")
            for i in range(n):
                f.write(", ".join([str(j) for j in l[i]]))
                f.write('\n')

        with open("outputs/outputs.txt",'a') as f:
            f.write("\n")
            f.write("U: ")
            f.write("\n")
            for i in range(n):
                f.write(", ".join([str(mat[i][j]) for j in range(n)]))
                f.write('\n')
        #Forward-substitution
        y = [0]*n
        for i in range(n):
            l[i].append(b[i])
        
        y = substitutions.forward_substitution(l)
        
        for i in range(n):
            mat[i][n] = y[i]

        #Back-substitution
        x = substitutions.back_substitution(mat)
        with open("outputs/outputs.txt",'a') as f:
            f.write("\n")
            f.write("X: ")
            f.write("\n")
            f.write("\n".join([str(j) for j in x]))

        
