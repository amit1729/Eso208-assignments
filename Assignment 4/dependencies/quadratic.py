import numpy as np
from sympy import *

def quadratic_spline(pts):
    n = pts.shape[0]
    ms = (n-1)*3
    A = np.zeros((ms,ms))
    V = np.zeros((ms,))
    j=0
    for i in range(0,2*(n-1),2):
        t = i//2
        A[i][j+0] = pts[t][0]**2
        A[i][j+1] = pts[t][0]
        A[i][j+2] = 1
        V[i] = pts[t][1]
        A[i+1][j+0] = pts[t+1][0]**2
        A[i+1][j+1] = pts[t+1][0]
        A[i+1][j+2] = 1
        V[i+1] = pts[t+1][1]
        j+=3
    k =1
    j=0
    for i in range(2*(n-1),ms-1,1):
        A[i][j+0] = 2*pts[k][0]
        A[i][j+1] = 1
        A[i][j+3] = -2*pts[k][0]
        A[i][j+4] = -1
        j+=3
        k+=1
    A[ms-1][0] = 1
    A = A[:,1:]
    A = A[:-1,:]
    V = V[:-1]
    coeff = np.linalg.solve(A,V)
    #coeff[0] = 0
    a = np.array([0])
    coeff = np.concatenate((a,coeff))
    #print(A)
    #print(V)
    #print(coeff)
    exprs = []
    x = symbols('x')
    for i in range(1,n,1):
        expr = coeff[3*(i-1)]*x**2 + coeff[3*(i-1)+1]*x + coeff[3*(i-1)+2]
        ra = (pts[i-1][0],pts[i][0])
        exprs.append([expr,ra])
    return exprs

