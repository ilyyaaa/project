for a in range (1,100):
    f=0
    for x in range (1,100):
        for y in range(1,100):
            if ((x<a) or (y<a) or (x+2*y>50))==0:
                f=1
    if f==0:
        print (a)
