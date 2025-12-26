## This is for optimisation techniques like gradient descent, log-loss maximisation and other techniques
from .losses import *

def weight_optimise(w,b,x,y,n):
    dw=0
    for i in range(n):
        dw+=-x[i]*(y[i]-(w*x[i]+b))
    dl_dw=(1/n)*dw

    return dl_dw
def bias_optimise(w,b,x,y,n):
    db=0
    for i in range(n):
        db+=-(y[i]-(w*x[i]+b))
    dl_db=(1/n)*db
    return dl_db

def gradient_descent(w,b,n,alpha,x,y):
    for i in range(n):
        w= w-alpha*weight_optimise(w,b,x,y,n)
        b= b-alpha*bias_optimise(w,b,x,y,n)
        print(f"The value of w and b are {w} and {b}")
    return w,b