l1=[1,2,3,4,5,6,7,8,9,10,11]
#print(l1[-1::-1])
l2=[12,13,14,15,6,17,18,19,20]
l3=list()
l4=list()
odd=l1[1::2]
even=l2[0::2]
#l3.append(odd)
#l4.append(even)
l3.extend(odd)
l4.extend(even)
print(l3)
print(l4)
print("enumeration type")
for i,item in enumerate(l3):
    print(i,item)

print("index wise")
for i in range(len(l3)):
    print(l3[i])