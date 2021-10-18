import numpy as np
def check(mat,n,eigval,eigvec):
    tt = np.round_(np.dot(mat - eigval*np.identity(n,dtype=float),eigvec), decimals=4)
    print(tt)