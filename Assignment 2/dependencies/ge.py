from dependencies import pivoting, scaling, substitutions

def ge(mat,pivot = False,scale = False,ts = False,LU_decompose = False):
    n = len(mat)
    if(pivot): mat = pivoting.pivot(mat)
    if(scale): mat = scaling.scale(mat,ts)

    if(pivot or scale):
        with open("outputs/outputs.txt",'w') as f:
            f.write("\n")
            f.write("Scaled/Pivoted Matrix:")
            f.write("\n")
            for i in range(n):
                f.write(", ".join([str(j) for j in mat[i]]))
                f.write('\n')
    else:
        with open("outputs/outputs.txt",'w') as f:
            f.write("")


    b = [i[n] for i in mat]
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

        
