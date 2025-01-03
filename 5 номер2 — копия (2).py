for n in range(1,1000):  
    n2=bin(n)[2:]
    if n%3==0:
        k=n2[-3:]
        n2+=k
    else:
          remain = n % 3 
    result_binary = bin(remain * 3)[2:]  
    n2+=result_binary
    R=int(n2,2)
    if R>=120:
    
        print(n)