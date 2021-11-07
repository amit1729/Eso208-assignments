import numpy as np
from sympy import *
from dependencies.eval import eval
from dependencies.cubic import cubic_spline
from dependencies.quadratic import quadratic_spline
from dependencies.linear import linear_spline
import matplotlib.pyplot as plt

inputs = ""
with open("input/input.txt",'r') as f:
    inputs = f.read().split("\n")
mat = []
n = len(inputs)

for i in range(1,n,1):
    if(inputs[i]=='evals'): break
    l = [float(j) for j in inputs[i].split(" ")]
    mat.append(l)
evals = []
i=i+1


for j in range(i,n,1):
    if(inputs[j]=='slope'): break
    evals.append(float(inputs[j]))
i = j+1

alpha = float(inputs[i].split(" ")[0])
beta1 = float(inputs[i].split(" ")[1])
pt = np.array(mat,dtype=float)

print("Enter the number corresponding to the method")
print("1 :->Linear Spline")
print("2 :->Quadratic Spline")
print("3 :->Natural Cubic Spline")
print("4 :->Not-a-Knot Cubic Spline")
print("5 :->Periodic Cubic Spline")
print("6 :->Clamped Cubic Spline")

n = int(input("Method number:- "))

if(n==1):
    spline = linear_spline(pt)
    evs = eval(spline,evals)
elif(n==2):
    spline = quadratic_spline(pt)
    evs = eval(spline,evals)
elif(n==3):
    spline = cubic_spline(pt)
    evs = eval(spline,evals)
elif(n==4):
    spline = cubic_spline(pt,not_a_knot=True)
    evs = eval(spline,evals)
elif(n==5):
    spline = cubic_spline(pt,periodic=True)
    evs = eval(spline,evals)
elif(n==6):
    spline = cubic_spline(pt,clamped=True,alpha=alpha,beta=beta1)
    evs = eval(spline,evals)
else: print("Invalid Number.......")
names = {
    1:"Linear Spline",
    2:"Quadratic Spline",
    3:"Normal Cubic Spline",
    4:"Not-a-Knot Cubic Spline",
    5:"Periodic Cubic Spline",
    6:"Clamped Cubic Spline"
}
with open("output/output.txt",'w') as f:
        f.write("\n")
        f.write(names[n])
        f.write("\n")
        for i in range(len(evals)):
            f.write(str(evals[i])+"  "+str(evs[i]))
            f.write("\n")

x = symbols('x')
le = len(spline)
for i in range(le):
    spline[i][0] = lambdify(x,spline[i][0])
for i in range(le):
    t = np.linspace(spline[i][1][0],spline[i][1][1],100)
    plt.plot(t, spline[i][0](t),color='blue')
plt.plot(pt[:,0],pt[:,1],'k*', label='given points')
plt.plot(evals,evs,'ro', label='evaluated points')
plt.legend()
#plt.show()
fig1 = plt.gcf()
fig1.savefig('output/Fitted_spline.png')
plt.close()