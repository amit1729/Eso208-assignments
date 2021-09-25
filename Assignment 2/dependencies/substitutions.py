
def forward_substitution(l):
    n = len(l)
    y = [0]*n
    y[0] = l[0][n]/l[0][0]
    for i in range(1,n,1):
        su = 0
        for j in range(0,i,1):
            su+= y[j]*l[i][j]
        y[i] = (l[i][n]-su)/l[i][i]
    return  y

def back_substitution(mat):
    n =len(mat)
    x = [0]*n
    x[n-1] = mat[n-1][n]/mat[n-1][n-1]
    for i in range(n-2,-1,-1):
        su = 0
        for j in range(i,n,1):
            su+= x[j]*mat[i][j]
        x[i] = (mat[i][n]-su)/mat[i][i]
    return x