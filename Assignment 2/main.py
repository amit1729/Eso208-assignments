from dependencies.ge import ge
from dependencies.crout import crout
from dependencies.cholesky import cholesky

inputs = ""
with open("inputs/inputs.txt",'r') as f:
    inputs = f.read().split("\n")
n = int(inputs[0])
mat = []
for i in range(1,n+1):
    l = [float(j) for j in inputs[i].split(" ")]
    mat.append(l)

print("Enter the number corresponding to the method")
print("1 :->Gauss Elimination")
print("2 :->Gauss Elimination(pivoting)")
print("3 :->Gauss Elimination(scaling and pivoting)")
print("4 :->LU decomposition via Gauss Elimination(without pivoting)")
print("5 :->LU decomposition via Gauss Elimination(with pivoting)")
print("6 :->LU decomposition via Crouts method(without pivioting")
print("7 :->Cholesky method")
n = int(input("Method number:- "))
if(n==1):
    ge(mat)
elif(n==2):
    ge(mat,pivot=True)
elif(n==3):
    print("Pivoting will be done using the matrix scaled by the highest number in the row but calculations will be done using the original matrix pivoted according to the scaled matrix")
    print("If you want calculations to be done using the scaled matrix. Enter 1")
    print("Else, Enter 0")
    k = int(input())
    if(k==1):
        ge(mat,scale=True,ts=True)
    else:
        ge(mat,scale=True)
elif(n==4):
    ge(mat,LU_decompose=True)
elif(n==5):
    ge(mat,pivot= True,LU_decompose=True)
elif(n==6):
    crout(mat)
elif(n==7):
    cholesky(mat)
else:
    print("Invalid Number!!!!")