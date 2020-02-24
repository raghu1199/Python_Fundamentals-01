def isPowerof3(num):
    while(num!=1):
        if(num%3!=0):
            return False
        num=num//3
    return True
print(isPowerof3(12))