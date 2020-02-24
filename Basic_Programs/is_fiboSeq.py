def is_fibo(seq):
    li=seq.split(",")
    n1,n2,n3,nth=0,0,0,0
    for i in range(len(li)-2):
        if n3==nth:
            n1=int(li[i])
            n2=int(li[i+1])
            n3=int(li[i+2])
            nth=n1+n2
        else:
            return False
    return True

seq1="6,6,12,18,30,58"
seq2="6,1,5,12,3,4"
seq3="0,1,1,2,5,7"
print(is_fibo(seq1))
print(is_fibo(seq2))
print(is_fibo(seq3))