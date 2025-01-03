def WIN1(s):
    return s + 1 >= 351 or s + 4 >= 351 or s * 2 >= 351

def LOSE1(s):
    return not WIN1(s) and WIN1(s + 1) and WIN1(s + 4) and WIN1(s * 2)
def WIN2(s):
     return LOSE1(s+1) or LOSE1(s+4) or  LOSE1(s*2)
for s in range(1, 351):
    if WIN2(s):
        print(s)
