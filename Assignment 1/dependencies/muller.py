from sympy import *
#
class muller:
    def __init__(self,function, x0, x1, x2,iterations, error):
        self.expr = sympify(function)
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.itr = iterations
        self.err = error
        self.res = []
        self.parse()
    
    def f(self,a):
        x = symbols('x')
        return self.expr.subs(x,a)
    
    def calc(self,x0,x1,x2):
        fx0 = self.f(x0)
        fx1 = self.f(x1)
        fx2 = self.f(x2)
        #print(fa,fb,fm)
        h0 = x1-x0
        h1 = x2-x1
        del0 = (fx1-fx0)/(x1-x0)
        del1 = (fx2-fx1)/(x2-x1)
        a = (del1-del0)/(h1+h0)
        b = a*h1+del1
        c = fx2
        d = abs(sqrt(b*b-4*a*c))
        if(b>0): x3 = x2+ (-2*c/(b+d))
        else: x3 = x2+(-2*c/(b-d))
        error = abs((x2-x3)/x3)
        dic = {
            "x0": x0, "x1": x1, "x2": x2,
            "fx0":fx0, "fx1":fx1, "fx2":fx2,
            "h0":h0, "h1":h1,
            "a":a, "b":b, "c":c,
            "x3": x3,
            "error": error*100
        }
        if(x3==nan):
            dic["x3"] = x2
            dic["error"] = 0.0
        return dic
        pass
        

    def parse(self):
        i =0
        lis = []
        x0 = self.x0
        x1 = self.x1
        x2 = self.x2
        err = 100
        while(i<self.itr and err>self.err):
            c = self.calc(x0,x1,x2)
            err = c["error"]
            x0 = x1
            x1 = x2
            x2 = c["x3"]
            i+=1
            lis.append(c)
            #print(c)
        self.res = lis


