from sympy import *

class false_position:
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
        fa = self.f(a)
        fb = self.f(b)
        m = a - (b-a)*fa/(fb-fa)
        fm = self.f(m)
        error =0
        anew = 0
        bnew =0
        #print(fa,fb,fm)
        if(fa == 0):
            anew = a
            bnew = a
        elif(fb == 0):
            anew = b
            bnew = b
        elif(fm == 0):
            anew = m
            bnew = m
        elif(fa*fm<0):
            anew = a
            bnew = m
            error = abs((anew-bnew))
        elif(fb*fm<0):
            anew = m
            bnew = b
            error = abs((anew-bnew))
        else: return 1
        dic = {
            "a":a, "b":b, "anew": anew, "bnew": bnew, "error": error*100
        }
        return dic
        
        

    def parse(self):
        i =0
        lis = []
        a = self.a
        b = self.b
        err = abs(a-b)*100/2
        while(i<self.itr and ( i==1 or err>self.err)):
            c = self.calc(a,b)
            if(type(c)==int):
                print("invalid Interval...")
                break
            err = c["error"]
            a = c["anew"]
            b = c["bnew"]
            i=i+1
            lis.append(c)
            #print(c)
        self.res = lis

