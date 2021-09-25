from sympy import *

class secant:
    def __init__(self,function, start, end,iterations, error):
        self.expr = sympify(function)
        self.a = start
        self.b = end
        self.itr = iterations
        self.err = error
        self.res = []
        self.parse()
    
    def f(self,a):
        x = symbols('x')
        return float(self.expr.subs(x,a))
    
    def calc(self,a,b):
        dic = {}
        fa = self.f(a)
        fb = self.f(b)
        m = b-fb*(b-a)/(fb-fa)
        err = abs((m-b)/m)
        dic["xk-1"] = a
        dic["xk"] = b
        dic["xk+1"] = m
        dic["error"] = err*100
        return dic
        #print(fa,fb,fm)
        

    def parse(self):
        i =0
        lis = []
        a = self.a
        b = self.b
        err = abs((a-b)/b)
        while(i<self.itr and ( i==1 or err>self.err)):
            c = self.calc(a,b)
            err = c["error"]
            a = c["xk"]
            b = c["xk+1"]
            lis.append(c)
            #print(c)
            i+=1
        self.res = lis

