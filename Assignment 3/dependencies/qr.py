import numpy as np

def qrdecompose(mat):
    A = np.copy(mat)
    n = mat.shape[0]
    Q = np.copy(A)
    R = np.zeros((n,n),dtype=float)
    for i in range(n):
        for j in range(i):
            R[j][i] = np.dot(Q[:,j].T,A[:,i])
        for j in range(i):
            Q[:,i] = Q[:,i]-Q[:,j]*R[j][i]
        R[i][i] = np.linalg.norm(Q[:,i])
        Q[:,i] /= R[i][i]
        
    return (Q,R)

def qreigen(mat,iter,err):
    n = mat.shape[0]
    A = np.copy(mat)
    error = 100
    for i in range(iter):
        if(error<=err): break
        Q,R = qrdecompose(A)
        A2 = np.dot(R,Q)
        idx = np.argmax(np.abs(A2))
        row = idx//3
        colmn = idx%3
        e1 = abs(A[row][colmn])
        e2 = abs(A2[row][colmn])
        error = abs(((e2-e1)/e2)*100)
        A = A2

    eigvalues = []
    res = {"itr":i,"value": eigvalues}
    for i in range(n):
        eigvalues.append(A[i][i])
    res["value"] = eigvalues
    return res
