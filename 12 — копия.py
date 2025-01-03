for n in range (1,1000):
    s='5'+n*'2'
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s=s.replace ('72','2',1)
        if '522' in s:
            s=s.replace ('522','27',1)
        if '2222' in s:
            s=s.replace ('2222', '5',1)
    sum = s.count('5')*5+s.count('7')*7+s.count('2')*2
    if sum==63:
            print (n)