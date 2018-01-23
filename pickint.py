def pick_int(x):
    if isinstance(x,float)==True:
        integ=x-int(x)
        if integ<0.5:
            x=int(x)
        else:
            x=int(x)+1
    return x
print pick_int(4.5)