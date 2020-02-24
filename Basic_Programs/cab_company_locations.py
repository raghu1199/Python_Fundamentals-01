s1=input(">>")
l1=[x for x in s1.split(" ")]
total_offices=int(l1[0])
start=int(l1[1])
end=int(l1[2])

s2=input(">>")
offices=[y for y in s2.split(" ")]
l3=[]

for i in range(start,end+1):
    for j in range(total_offices):
        val=int(offices[j])
        if i==val:
            l3.append(str(i))

print(l3)
print(' '.join(l3))

