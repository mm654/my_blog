import math
def is_prime(x):
    k=2
    flag=0
    while(k<=math.sqrt(x)):
        if x%k==0:
            flag=1
            break
        k=k+1
    if flag==1:
        return x
print filter(is_prime,range(1,101))