def convert(num):
    li=list()
    while(num>0):
        rem=num%10
        li.append(rem)
        num=num//10
    return li
def singleD(num):
    res_li=convert(num)
    print("digits:",res_li)
    res=str(sum(res_li))
    print("sum of digits:",res)
    res_li.clear()
    if len(res)==1:
        return res
    else:
        return singleD(int(res))

singleD(64768567)
