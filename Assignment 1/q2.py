from dependencies import muller, bairstow
from sympy import *

print("Notes:\n (1) Kindly use x as variable in the equations.\n (2) use '**' for power\n (3) Ex1: 5*x**2+2*x+1\n (4) Ex2: exp(-x)-x")
s = input("Equation: ")
print("Enter the respected given below numbers for preferred method")
print("Muller:- 1")
print("Bairstow:- 2")
n = int(input("Method Number: "))
if(n==1):
    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = muller.muller(s,x0,x1,x2,itr,err).res
    root = res[-1]["x3"]
    print("#########################################################################")
    print(root)
    with open('output/output.txt', 'w') as f:
        f.write("Root: "+str(root))
        f.write('\n')
        for i in res[0].keys():
            f.write(i+" ")
        f.write('\n')

        for k in res:
            for i in k.keys():
                f.write(str(k[i])+" ")
            f.write('\n')

    

if(n==2):
    r = float(input("r: "))
    s1 = float(input("s: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))
    res = bairstow.bairstow(s,itr,err,r,s1)
    print("#########################################################################")
    with open('output/output.txt', 'w') as f:
        for i in res:
            if i[1]!=0:
                f.write(str(i[0])+"+"+str(i[1])+"I")
            else:
                f.write(str(i[0]))
            f.write('\n')
    
x = symbols('x')
y = sympify(s)
p1 = plot(y, (x,-4,4), show = False)
p1.show()
p1.save('output/fx_vs_x.png')
