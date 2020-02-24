def fibonacci(nterms):
    n1=0
    n2=1
    count=0
    if nterms==1:
        print("fibo seq:",1)
    else:
        print("fibo seq:")
    while count<=nterms:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2;
        n2=nth
        count+=1

def fibo(nth):
    if nth==0:
        return 0
    if nth==1:
        return 1
    else:
        return fibo(nth-1)+fibo(nth-2)

def fibo_dynamic(nth):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,nth+1,1):
        seq=f[i-1]+f[i-2]
        f.append(seq)
    print(f)
    return f[nth]


print(fibo_dynamic(9))
#print(fibo(9))
#fibonacci(10)