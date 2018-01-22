def boundary():
    sum=1
    x=2
    n=31
    while n>0:
      sum=sum*x
      n=n-1
    return sum

T=int(raw_input())
L=[]
for i in range(0,T):
    A,B,C=map(int,raw_input().split())
    for x in [A,B,C]:
        if x<-boundary() or x>boundary():
          print'the enter is wrong'
    L.append(A)
    L.append(B)
    L.append(C)
i=0
k=1
while i+2<len(L):
    if L[i]+L[i+1]>L[i+2]:
        print'Case #',k,':',True
    else:
        print'Case #',k,':',False
    i=i+3
    k=k+1

   