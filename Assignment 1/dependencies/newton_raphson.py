from sympy import *

class newton_raphson:
    def __init__(self,function, start,iterations, error):
        self.expr = sympify(function)
        self.a = start
        self.itr = iterations
        self.err = error
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
        dic["fai"] = fda
        dic["error"] = abs((anew-a)/anew)
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
            print(dic["ai"]," ",dic["fai"]," ",dic["fdash"]," ",dic["ai+1"]," ",dic["error"]," ")
        return lis

s = "600*x**4-550*x**3+200*x**2-20*x-1"
start = 0.1
end = 1
iterations = 20
error = 0.05/100
fal = newton_raphson(s,start,iterations,error)