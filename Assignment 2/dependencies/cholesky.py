import substitutions

def cholesky(a):
    n = len(a)
    l = [[0]*n for i in range(n)]

    for k in range(n):
        for i in range(k):
            sum1 = 0
            for j in range(i):
                sum1+= l[i][j]*l[k][j]
            if(l[i][i]!=0):
                l[k][i] = (a[k][i]-sum1)/l[i][i]
        sum1 = 0
        for j in range(k):
            sum1+=l[k][j]*l[k][j]
        l[k][k] = (a[k][k]-sum1)**0.5
    
    u = [i.copy() for i in l]
    for i in range(n):
        for j in range(i):
            temp= u[i][j]
            u[i][j] = u[j][i]
            u[j][i] = temp
    print(l)
    print(u)
    for i in range(n):
        l[i].append(a[i][n])
    y = substitutions.forward_substitution(l)
    print(y)
    for i in range(n):
        u[i].append(y[i])
    x = substitutions.back_substitution(u)
    print(x)

mat = [[6,15,55,76],[15,55,225,295],[55,225,979,1259]]
cholesky(mat)