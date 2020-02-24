def sum_num(num,req_sum):
    li=list()
    sum=0
    for i in range(len(num)-2):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                a=num[i]
                b=num[j]
                c=num[k]
                sum=a+b+c
                if sum==req_sum:
                    s1=[a,b,c]
                    li.append(s1)
    return li

num=[1,-1,2,3,-2,6,8,7,2,4,6]
print(sum_num(num,5))