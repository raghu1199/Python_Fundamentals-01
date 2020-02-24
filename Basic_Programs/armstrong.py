
def digits(num):
    i=0
    while(num>0):
        num=num//10
        i=i+1
    print("digits:%d"%i)
    return i

def resto(rem,d):
    base=1
    for i in range(d):
        base=rem*base
    print(f"{rem} resto {d} is:{base}")
    return  base



def isArmstrong(num):
    temp=num
    sum=0
    d=digits(num)
    while(num>0):
        rem=num%10
        powered=resto(rem,d)
        sum=sum+powered
        num=num//10
    if(sum==temp):
        print("number is Armstrong")
    else:
        print("Not a armstrong number")


n=int(input("enter number"))
isArmstrong(n)