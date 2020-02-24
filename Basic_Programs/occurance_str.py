def count_raghu(st):
    count=0
    for i in range(len(st)):
        if(st[i:i+5]=='raghu'):
            count+=1
    return count

count=count_raghu("raghu is good boy.raghu is quite cool nature of raghu is best ever")
print(count)