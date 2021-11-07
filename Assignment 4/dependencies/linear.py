import numpy as np
from sympy import *

def linear_spline(pts):
    n = pts.shape[0]
    exprs = []
    x = symbols('x')
    for i in range(1,n,1):
        expr = ((x-pts[i-1][0])*pts[i][1]/(pts[i][0]-pts[i-1][0])) + ((x-pts[i][0])*pts[i-1][1]/(pts[i-1][0]-pts[i][0]))
        ra = (pts[i-1][0],pts[i][0])
        exprs.append([expr,ra])
    return exprs
