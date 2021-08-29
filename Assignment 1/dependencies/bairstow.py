from sympy import *

def quadroot(r,s):
    disc = r**2+4*s
    if disc>0:
        r1 = (r+(disc**0.5))/2
        r2 = (r-(disc**0.5))/2
        i1,i2=0,0
    else:
        r1 = r/2
        r2 = r1
        i1 = ((abs(disc))**0.5)/2
        i2 = -i1
    return (r1,i1,r2,i2)

def calc(a,nn,es,rr,ss,maxit):
    lis = []
    b = [0]*(nn+1)
    c = [0]*(nn+1)
    s =ss
    n =nn
    r =rr
    re = [0]*nn
    im = [0]*nn
    iter,ea1,ea2 = 0,1,1
    while(1):
        if(n<3 or iter>maxit): break
        while(1):
            #print(iter)
            iter+=1
            b[n] = a[n]
            b[n-1] = a[n-1]+r*b[n]
            c[n] = b[n]
            c[n-1] = b[n-1]+r*c[n]
            i = n-2
            while(i>=0):
                b[i] = a[i]+r*b[i+1]+s*b[i+2]
                c[i] = b[i]+r*c[i+1]+s*c[i+2]
                i-=1
            #print("b:", b)
            #print("c:", c)
            #print("#########################################################################")
            det = c[2]*c[2]-c[3]*c[1]
            if det!=0:
                dr = (-b[1]*c[2]+b[0]*c[3])/det
                ds = (-b[0]*c[2]+b[1]*c[1])/det
                r=r+dr
                s=s+ds
                #print(r)
                #print(s)
                if r!=0: ea1 = abs(dr/r)*100
                if s!=0: ea2 = abs(ds/s)*100
            else:
                r+=1
                s+=1
                iter = 0
            if (ea1<es and ea2<es) or iter>=maxit: break
        re[n-1], im[n-1], re[n-2], im[n-2] = quadroot(r,s)
        lis.append((re[n-1], im[n-1]))
        lis.append((re[n-2], im[n-2]))
        n = n-2
        i = 0
        while(i<=n):
            a[i] = b[i+2]
            i+=1
    if iter<maxit:
        if n==2:
            r = -a[1]/a[2]
            s = -a[0]/a[2]
            re[n-1], im[n-1], re[n-2], im[n-2] = quadroot(r,s)
            lis.append((re[n-1], im[n-1]))
            lis.append((re[n-2], im[n-2]))
        else:
            re[n-1] = -a[0]/a[1]
            im[n-1] = 0
            lis.append((re[n-1], im[n-1]))
    return lis

def bairstow(function,itr,err,r,s):
    x = symbols('x')
    p = poly(sympify(function),x)
    lis = p.all_coeffs()
    lis.reverse()
    lis  = [float(i) for i in lis]
    nn = len(lis)-1
    answer  = calc(lis,nn,err,r,s,itr)
    return answer
    



    