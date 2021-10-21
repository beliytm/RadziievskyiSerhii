import math
import matplotlib.pyplot as plt
from scipy import optimize
from numpy import *
x=linspace(-2,1,100)
y=cos(x+0.5)-2
y1=linspace(-2,0,100)
x1=0.5*sin(y)-0.5
plt.plot(x,y,x1,y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of functions')
plt.legend(['y=cos(x-0.5)-2', 'x=0.5sin(y)-0.5'],loc='upper left')
plt.grid(True)
plt.show()
x0=-1.
y0=-1.
def f1(y):
    return  -1/2 + math.sin(y)/2
def f2(x):
    return math.cos(x+0.5)-2
def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.0001)
def f(x):
    return math.cos(x[0] +0.5) - x[1] - 2, math.sin(x[1]) - 2*x[0] -1
s = optimize.root(f, [-1,-1.95], method = 'hybr')
print('Calculation check\n',s.x)
