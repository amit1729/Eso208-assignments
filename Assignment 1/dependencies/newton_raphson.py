from sympy import *

class newton_raphson:
    def __init__(self,function, start,iterations, error):
        self.expr = sympify(function)
        self.a = start
        self.itr = iterations
        self.err = error
        self.res = []
        self.parse()
    
    def f(self,a):
        x = symbols('x')
        return float(self.expr.subs(x,a))
    
    def fdash(self,a):
        x = symbols('x')
        expr_diff = Derivative(self.expr, x)
        return float(expr_diff.doit().subs(x,a))

    def calc(self,a):
        fa = self.f(a)
        fda = self.fdash(a)
        anew = a - fa/fda
        dic = {}
        dic["ai"] = a
        dic["ai+1"] = anew
        dic["fdash"] = fda
        dic["fai"] = fa
        dic["error"] = abs((anew-a)/anew)*100
        return dic
        

    def parse(self):
        i =0
        lis = []
        a = self.a
        err = 100
        while(i<self.itr and ( i==1 or err>self.err)):
            dic = self.calc(a)
            err = dic["error"]
            a = dic["ai+1"]
            lis.append(dic)
            i=i+1
            #print(dic)
        self.res= lis

