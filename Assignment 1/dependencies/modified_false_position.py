from sympy import *

class modified_false_position:
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
    
    def calc(self,a,b,ia,ib):
        fa = self.f(a)
        fb = self.f(b)
        #print(fa,fb)
        m = (a*fb-b*fa)/(fb-fa)
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
            ib=0
            ia+=1
            if(ia>2):
                fa = fa/2**(ia-2)
                m = (a*fb-b*fa)/(fb-fa)
            fm = self.f(m)
            if(fa*fm<0):
                anew = a
                bnew = m
                error = abs((anew-bnew))
            else:
                ia = 0
                ib+=1
                anew = m
                bnew = b
                error = abs((anew-bnew))
        elif(fb*fm<0):
            ia=0
            ib+=1
            if(ib>2):
                fb = fb/2**(ib-2)
                m = (a*fb-b*fa)/(fb-fa)
            fm = self.f(m)
            if(fb*fm<0): 
                anew = m
                bnew = b
                error = abs((anew-bnew))
            else:
                ib=0
                ia+=1
                anew = a
                bnew = m
                error = abs((anew-bnew))
        else: return 1
        dic = {
            "a":a, "b":b, "anew": anew, "bnew": bnew, "error": error*100, "ia":ia, "ib": ib
        }
        return dic
        

    def parse(self):
        i =0
        ia = 0
        ib =0
        lis = []
        a = self.a
        b = self.b
        err = abs(a-b)*100/2
        while(i<self.itr and ( i==1 or err>self.err)):
            c = self.calc(a,b,ia,ib)
            if(type(c)==int):
                print("invalid Interval...")
                break
            err = c["error"]
            a = c["anew"]
            b = c["bnew"]
            ia = c["ia"]
            ib = c["ib"]
            i=i+1
            lis.append(c)
            #print(c)
        self.res = lis

