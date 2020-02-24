def isPalindrom(num):
    original=num
    reverse=0
    while(num>0):
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    if(original==reverse):
        return True
    else:
        return False

n=int(input("enter num to check palindrom"))
print(isPalindrom(n))