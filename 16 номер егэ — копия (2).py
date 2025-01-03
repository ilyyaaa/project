import sys

def f(n):
    if n<11:
        return n
    if n>=11:
        return n+f(n-1)
sys.setrecursionlimit(10000)  
print (f(2024)-f(2021))