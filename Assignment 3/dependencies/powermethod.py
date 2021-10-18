import numpy as np

def powermethod(mat, iter, err, inverse= False):
    A = np.copy(mat)
    if(inverse): A = np.linalg.inv(A)

    n = A.shape[0]
    V = np.ones((n,1))

    error = 100
    S = 1
    for i in range(iter):
        #print(S,error)
        if(error<=err): break
        V = np.dot(A,V)
        S1 = np.abs(V).max()
        V = V/S1
        error = abs(((S1-S)/S1)*100)
        S = S1
    
    if(inverse): S = 1/S
    dic = {"itr":i,"value": S, "vector": V}
    return dic

def shiftedpower(mat,iter,err,shift=None):
    out = []
    n = mat.shape[0]
    if(shift == None):
        A = np.copy(mat)
        lis = []
        for i in range(n):
            lis.append(A[i][i])
        lis.sort(key=abs)
        lis.pop(0)
        lis.pop(-1)
        for elem in lis:
            A = np.copy(mat)
            A = A - elem*(np.identity(n,dtype=float))
            res = powermethod(A,iter,err,inverse=True)
            res["value"] = res["value"]+elem
            out.append(res)
    else:
        A = np.copy(mat)
        A = A - shift*(np.identity(n,dtype=float))
        res = powermethod(A,iter,err,inverse=True)
        res["value"] = res["value"]+shift
        out.append(res)
    return out
