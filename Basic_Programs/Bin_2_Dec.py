def dec_bin(dec):
    bin=[]
    rem=0
    i=0
    while(dec>0):
        rem=dec%2
        bin.append(rem)
        dec=dec//2
    l=len(bin)-1
    print(bin)
    print("bin is:")
    for i in range(len(bin)-1,-1,-1):
        print(bin[i],end="")



def bin_dec(bin):
    dec=0
    rem=0
    base=1
    while(bin>0):
        rem=bin%10
        dec=dec+base*rem
        base=base*2
        bin=bin//10

    print("dec is:",dec)

n=int(input("enter binary number:"))
bin_dec(n)
n1=int(input("enter decimal number:"))
dec_bin(n1)

