import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

x = sp.symbols('x')

#Taking input of the function

f_string = input("input your function in x !")

f = sp.sympify(f_string)

#Integration or differentiation?

m = input("What to do?")
#For Integration
if m == "int":
      print("Function given by you", f,
            "you opt to integrate the given function")
      a = input("Put the lower limit !")
      b = input("Put the upper limit !")
      n = sp.integrate(f, (x, a, b))

      print(n)
      l=sp.lambdify(x,n ,modules=["numpy"])
      print(l)
      
#For Differentiation
if m == 'diff':

      print("Function given by you", f,
            "you opt to differentiate the given function")
      u = sp.diff(f, x)
      print(u)
      k = sp.sympify(u)
# Otherwise nothing, get lost
else:
      print("okay")
u = sp.diff(f, x)
k = sp.sympify(u)
t = sp.lambdify(x, f, modules=['numpy'])
w = sp.lambdify(x,k, modules=["numpy"])

x_vals = np.linspace(-10, 20, 100000)
y_vals = t(x_vals)

plt.grid(True)

plt.plot(x_vals, y_vals, "maroon",label=f_string)
plt.legend()

if m == "diff":
      p = input("Type the value of x where you want the tangent ")

      x1 = float(p)
      y1 = t(x1)
      plt.scatter(x1, y1)
      #calculating the slope at x1:-
      q = w(x1)
      c = (y1 - q * x1)
      x2 = np.linspace(0, 20, 100)
      y2 = q * x2 + c
      plt.plot(x2, y2, "black",label="Tangent at given x")

if m=="int":
      

      xfill=np.linspace(float(a),float(b),1000)
      yfill=t(xfill)
      plt.fill_between(xfill,yfill,color="gold",alpha=0.6,label='Area under the curve')
      
else:
      print("okay")
      
plt.legend()
plt.show()