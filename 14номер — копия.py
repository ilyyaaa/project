k=0
s=2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
while s>0:
    if s%9!=0:
        k=k+1
    s=s//9
print(k)
