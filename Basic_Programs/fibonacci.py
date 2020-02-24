def ispow2(n):
    return n>0 and (n&(n-1))==0

def isPow2(n):

    while(n!=1):
        if(n%2!=0):
            return False
        n=n//2
    return True
n=int(input("enter num to check pow2:"))
print(ispow2(n))
print(isPow2(n))