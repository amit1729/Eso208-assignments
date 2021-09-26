from dependencies import substitutions

def crout(a):
    n = len(a)
    l = [[0]*n for i in range(n)]
    u = [[0]*n for i in range(n)]
    for i in range(n):
        u[i][i] = 1
    
    for j in range(n):
        for i in range(j,n,1):
            sum1 = 0
            for k in range(j):
                sum1+=l[i][k]*u[k][j]
            l[i][j] = a[i][j]-sum1
        #print(l)
        for i in range(j,n,1):
            sum1 = 0
            for k in range(j):
                sum1 += l[j][k]*u[k][i]
            if(l[j][j]!=0):
                u[j][i] = (a[j][i]-sum1)/l[j][j]
        #print(u)
    
    with open("outputs/outputs.txt",'w') as f:
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
            f.write(", ".join([str(j) for j in u[i]]))
            f.write('\n')

    for i in range(n):
        l[i].append(a[i][n])
    y = substitutions.forward_substitution(l)
    
    for i in range(n):
        u[i].append(y[i])
    x = substitutions.back_substitution(u)
    
    with open("outputs/outputs.txt",'a') as f:
        f.write("\n")
        f.write("X: ")
        f.write("\n")
        f.write("\n".join([str(j) for j in x]))


        