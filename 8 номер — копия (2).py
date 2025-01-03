alf = 'клнтэ' #в алфавитном порядке обязательно!!!
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        s=x1+x2+x3+x4+x5+x6
                        k+=1
                        if k<1000:
                            print (k,s)
