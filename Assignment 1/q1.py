from dependencies import bisection, false_position, modified_false_position, newton_raphson,secant
import matplotlib.pyplot as plt
from sympy import *


print("Notes:\n (1) Kindly use x as variable in the equations.\n (2) use '**' for power\n (3) Ex1: 5*x**2+2*x+1\n (4) Ex2: exp(-x)-x")
s = input("Equation: ")
print("Enter the respected given below numbers for preferred method")
print("Bisection:- 1")
print("False-position:- 2")
print("Modified-false-position:- 3")
print("Newton-Raphson:- 4")
print("Secant:- 5")
n = int(input("Method Number: "))
root = 0
if(n==1):
    xl = float(input("xl: "))
    xu = float(input("xu: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = bisection.bisection(s,xl,xu,itr,err).res
    root = (res[-1]["anew"]+res[-1]["bnew"])/2

if(n==2):
    xl = float(input("xl: "))
    xu = float(input("xu: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = false_position.false_position(s,xl,xu,itr,err).res
    root = (res[-1]["anew"]+res[-1]["bnew"])/2


if(n==3):
    xl = float(input("xl: "))
    xu = float(input("xu: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = modified_false_position.modified_false_position(s,xl,xu,itr,err).res
    root = (res[-1]["anew"]+res[-1]["bnew"])/2

if(n==4):
    x0 = float(input("x0: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = newton_raphson.newton_raphson(s,x0,itr,err).res
    root = res[-1]["ai+1"]

if(n==5):
    xl = float(input("x-1: "))
    xu = float(input("x0: "))
    itr = int(input("Maximum iterations: "))
    err = float(input("error(%): "))/100
    res = secant.secant(s,xl,xu,itr,err).res
    root = res[-1]["xk+1"]
print("############################################################")
print("Root: ",root)

x = []
y = []
for i in range(len(res)):
    if i ==0:continue
    x.append(i+1)
    y.append((res[i])["error"]*100)
plt.plot(x,y)
plt.xlabel('Iterations')
plt.ylabel('error(%)')
fig1 = plt.gcf()
plt.show()
fig1.savefig('output/itr_vs_error.png')
plt.close()

x = symbols('x')
y = sympify(s)
p1 = plot(y, (x,-0.1,0.3), show = False)
p1.show()
p1.save('output/fx_vs_x.png')
#print(res)