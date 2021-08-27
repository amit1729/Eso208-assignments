from sympy import *
s = input()
x, y = symbols('x y')
expr = sympify(s, evaluate = False)
print("Expression : {} ".format(expr))
print(type(int(expr.subs([(x,1),(y,1)]))))
# Use sympy.Derivative() method 
expr_diff = Derivative(expr, x)  
      
print("Derivative of expression with respect to x : {}".format(expr_diff))  
dev = expr_diff.doit()
print(expr_diff.doit().subs([(x,1),(y,1)]))