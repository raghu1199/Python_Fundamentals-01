def single_occurance(list1):
    count=dict()
    list2=list()
    for item in list1:
        if(item in count):
            count[item]+=1
        else:
            count[item]=1
    print(count)
    for j in count:
        if count[j]==1:
            list2.append(j)
    return list2

num=[1,3,2,5,2,6,3,4,8,9,5,7]
print(single_occurance(num))