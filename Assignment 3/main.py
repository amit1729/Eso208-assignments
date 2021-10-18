from dependencies.powermethod import powermethod, shiftedpower
from dependencies.qr import qrdecompose, qreigen
import numpy as np
inputs = ""
with open("input/input.txt",'r') as f:
    inputs = f.read().split("\n")
r = int(inputs[0])
mat = []
for i in range(1,r+1):
    l = [float(j) for j in inputs[i].split(" ")]
    mat.append(l)
itr = int(inputs[r+1])
err = float(inputs[r+2])
if(len(inputs)>=r+4):
    if(inputs[r+3]!=""): shift = float(inputs[r+3])
    else: shift = None
else: shift = None

mat = np.array(mat,dtype=float)

print("Enter the number corresponding to the method")
print("1 :->Direct Power Method")
print("2 :->Inverse Power Method")
print("3 :->Shifted power Method")
print("4 :->QR method")

no = int(input("Method number:- "))
if(no==1):
    res = powermethod(mat,itr,err)
    with open("outputs/outputs.txt",'w') as f:
        f.write("\n")
        f.write("Direct Power Method")
        f.write("\n\n")
        f.write("Eigenvalue:")
        f.write("\n")
        f.write(str(res["value"]))
        f.write("\n\n")
        f.write("Eigenvector:")
        f.write("\n")
        f.write("\n".join([str(i) for i in list(res["vector"].flatten())]))
        f.write("\n\n")
        f.write("Iterations:")
        f.write("\n")
        f.write(str(res["itr"]))
        f.write("\n\n")
if(no==2):
    res = powermethod(mat,itr,err,inverse=True)
    with open("outputs/outputs.txt",'w') as f:
        f.write("\n")
        f.write("Inverse Power Method")
        f.write("\n\n")
        f.write("Eigenvalue:")
        f.write("\n")
        f.write(str(res["value"]))
        f.write("\n\n")
        f.write("Eigenvector:")
        f.write("\n")
        f.write("\n".join([str(i) for i in list(res["vector"].flatten())]))
        f.write("\n\n")
        f.write("Iterations:")
        f.write("\n")
        f.write(str(res["itr"]))
        f.write("\n\n")
if(no==3):
    res = shiftedpower(mat,itr,err,shift)
    with open("outputs/outputs.txt",'w') as f:
        f.write("\n")
        f.write("Shifted Power Method")
        for r in res:
            f.write("\n\n")
            f.write("Eigenvalue:")
            f.write("\n")
            f.write(str(r["value"]))
            f.write("\n\n")
            f.write("Eigenvector:")
            f.write("\n")
            f.write("\n".join([str(i) for i in list(r["vector"].flatten())]))
            f.write("\n\n")
            f.write("Iterations:")
            f.write("\n")
            f.write(str(r["itr"]))
            f.write("\n\n")
if(no==4):
    res = qreigen(mat,itr,err)
    with open("outputs/outputs.txt",'w') as f:
        f.write("\n")
        f.write("QR Method")
        f.write("\n\n")
        f.write("Eigenvalues:")
        f.write("\n")
        f.write("\n".join([str(i) for i in res["value"]]))
        f.write("\n\n")
        f.write("Iterations:")
        f.write("\n")
        f.write(str(res["itr"]))
        f.write("\n\n")
