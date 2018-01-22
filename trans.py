
def trans(name):
    L=[]
    if name[:1].islower():
        L.append(name[:1].upper())
    else:
        L.append(name[:1])
    for x in name[1:]:
        if x.isupper():
            L.append(x.lower())
        else:
            L.append(x)
    return ''.join(L)   
#print trans('aDas')
print map(trans,['adam', 'LISA', 'barT'])