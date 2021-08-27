from sympy import *

class bisection:
    def __init__(self,function, start, end,iterations, error):
        self.expr = sympify(function)
        self.a = start
        self.b = end
        self.itr = iterations
        self.err = error
        self.parse()
    
    def f(self,a):
        x = symbols('x')
        return float(self.expr.subs(x,a))
    
    def calc(self,a,b):
        m = (a+b)/2
        fm = self.f(m)
        fa = self.f(a)
        fb = self.f(b)
        #print(fa,fb,fm)
        if(fa == 0): return (a,b,a,a,0)
        if(fb == 0): return (a,b,b,b, 0)
        if(fm == 0): return (a,b,m,m, 0)
        if(fa*fm<0): return(a,b,a,m, abs((a-m)/2))
        if(fb*fm<0): return (a,b,m,b, abs((b-m)/2))
        else: return 1
        

    def parse(self):
        i =0
        lis = []
        a = self.a
        b = self.b
        err = abs(a-b)/2
        while(i<self.itr and ( i==1 or err>self.err)):
            c = self.calc(a,b)
            if(type(c)==int):
                print("invalid Interval...")
                break
            err = c[4]
            a = c[2]
            b = c[3]
            i+=1
            lis.append(c)
            print(c)
        return lis

s = "600*x**4-550*x**3+200*x**2-20*x-1"
start = 0.1
end = 1
iterations = 20
error = 0.05/100
fal = bisection(s,start,end,iterations,error)


