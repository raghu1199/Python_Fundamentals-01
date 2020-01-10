friends2=["Raghu","rahul","ashu","sajskj","asssd"]
new=["ashok","milan","chetana"]

print(len(friends2))
print("friends[2]:",friends2[0])
print("max of friends2:",max(friends2))
print(friends2[0:3])   #0 to 2nd
print(friends2[1:-2])  # rahul to ashu 1 to end except last two
friends2.append("ronak")
print(friends2)
friends2.remove("rahul")
print(friends2)
print("insert at 2:",end=" ")
friends2.insert(2,new)
print(friends2)
print("extend:",end=" ")
friends2.extend(new)
print(friends2)


friends=[['rolf',24],['bob',30],['anne',27]]
print(friends[0][1])
print(friends[1][0])
print(friends[2])
friends.append(["rahul",23])
print(friends)
friends.remove(["bob",30])
print(friends)
new=["ashok","milan","chetana"]
friends.insert(1,new)
print(friends)

print("iteration on list:")
for friend in friends:
    print(friend)
print("index wise access")
for i in range(len(friends)):
    print(f"friends[{i}]:",friends[i])

print("ashu" in friends2)
print("chintan" in friends2)

flist=['raghu','rahul','nikhil']
friends_str="-".join(flist)
str="raghu rahul nikhil bhardwaj"
f_list=str.split(",")
print("list from string:",f_list,end=" ")
print("after join:",friends_str)

print("opertaions on nums:")
nums=[1,5,3,2,4,7]
nums2=sorted(nums)
print("original after sorted in new list:",nums)
print("sorted new list:",nums2)
nums.sort()
print("in place sort",nums)
print("max:",max(nums))
print("sum:",sum(nums))

"""
In python Only list are mutable ->they allow modification on themself ,it while other tuple,set,variables all are immutable
in python ->they do not allow to change if you change its value they become new object
"""


list1=[3,4,56,901,2]
print("list1:",list1)
print("list id before modification:",id(list1))
list1.append(45)
list1.extend([2,3,6,45])
print(list1)
print("id of modified list:",id(list1))



