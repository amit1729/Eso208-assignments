import numpy as np
from sympy import *

def eval(exprs, lis):
    n = len(lis)
    x = symbols('x')
    ans = []
    for i in range(n):
        a = lis[i]
        for expr in exprs:
            if(a>=expr[1][0] and a <=expr[1][1]):
                temp = float(expr[0].subs(x,a))
                ans.append(temp)
    print(ans)
    return ans