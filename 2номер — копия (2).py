for x in range(2):
    for y in range(2):
        for w in range (2):
            for z in range(2):
                if (y and(x or z)or (not(y or z)) or w)==0:
                    print(x,y,w,z)