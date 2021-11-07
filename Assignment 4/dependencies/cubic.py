import numpy as np
from sympy import *

def sigmas(pts, not_a_knot = False, periodic = False, clamped = False, alpha =0,beta =0):
    n = pts.shape[0]
    for i in range(1,n,1):
        pts[i][2] = pts[i][0]-pts[i-1][0]
        pts[i][3] = (pts[i][1]-pts[i-1][1])/pts[i][2]
    A = np.zeros((n,n))
    V = np.zeros((n,))
    A[0][0] = 1
    A[n-1][n-1] = 1
    V[0] = 0
    V[n-1] = 0
    #print(pts)
    if(not_a_knot):
        A[0][0] = pts[2][2]
        A[0][1] = -(pts[1][2]+pts[2][2])
        A[0][2] = pts[1][2]
        A[n-1][n-1] = pts[n-2][2]
        A[n-1][n-2] = -(pts[n-1][2]+pts[n-2][2])
        A[n-1][n-3] = pts[n-1][2]
    if(clamped):
        A[0][0] = 2*pts[1][2]
        A[0][1] = pts[1][2]
        A[n-1][n-1] = 2*pts[n-1][2]
        A[n-1][n-2] = pts[n-1][2]
        V[0] = 6*(pts[1][3]-alpha)
        V[n-1] = 6*(beta-pts[n-1][3])
    
    if(periodic):
        A[0][0] = 2*pts[1][2]
        A[0][1] = pts[1][2]
        A[0][n-1] = 2*pts[n-1][2]
        A[0][n-2] = pts[n-1][2]
        A[n-1][0] = 1
        A[n-1][n-1] = -1
        V[0] = 6*(pts[1][3]-pts[n-1][3])
    #print(A)
    for i in range(1,n-1,1):
        A[i][i-1] = pts[i][2]
        A[i][i+1] = pts[i+1][2]
        A[i][i] = 2*(pts[i+1][2]+pts[i][2])
        V[i] = 6*(pts[i+1][3]-pts[i][3])
    sig = np.linalg.solve(A,V)
    print(sig)
    return (pts,sig)

def cubic_spline(pts, not_a_knot = False, periodic = False, clamped = False, alpha =0,beta =0):
    n = pts.shape[0]
    pts = np.hstack((pts,np.zeros((n,2))))
    pts,sig = sigmas(pts, not_a_knot = not_a_knot, periodic = periodic, clamped = clamped, alpha =alpha,beta =beta)
    exprs = []
    x = symbols('x')
    for i in range(1,n,1):
        A = sig[i]/(6*pts[i][2])
        C = (pts[i][1]/pts[i][2]) - (sig[i]*pts[i][2]/6)
        B = sig[i-1]/(6*pts[i][2])
        D = (pts[i-1][1]/pts[i][2]) - (sig[i-1]*pts[i][2]/6)
        expr = A*(x-pts[i-1][0])**3 - B*(x-pts[i][0])**3 + C*(x-pts[i-1][0])-D*(x-pts[i][0])
        ra = (pts[i-1][0],pts[i][0])
        #print(expr)
        exprs.append((expr,ra))
    return exprs
