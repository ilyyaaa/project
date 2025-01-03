for n in range(1,1000):  
    n2=bin(n)[2:]
    remain=n2.count('1')%2
    n2+=str(remain)
    remain2=n2.count('1')%2
    n2+=str(remain2)
    R=int(n2,2)
    if R>123:
    
        print(R)