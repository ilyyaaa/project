import sys
def f(n):
    if n==1:
        return 1
    elif n>1:
        return n*f(n-1)
sys.setrecursionlimit(10000) 
print ((f(2023)-f(2022))/f(2020))


