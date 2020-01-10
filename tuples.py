tuple1=('history','math','physics')
print(tuple1[1])
#tuple1[0]="art"  gives error
s_tuple="rolf","bob"
print(s_tuple)
t2=tuple1
print(t2 is tuple1)
print(t2)
print('math' in tuple1)   #True
f1=("raghu","rahul","jayant")
f2=("ronak","ashu")
print("id of f2 before:",id(f2))
f2=f1+f2
print("id of f2 after add two tuples:",id(f2))
print("after add two tuple:",f2)
li=[1,2,3,4,5]
t=tuple(li)
print("max:",max(t),"sum:",sum(t),"len:",len(t))
a=('pythpnzz','zzzz')
b=('abc','abcd')
print((a>b)-(a<b))

"""
To change or modify tuple first convert tuple to list ->do
moodification and then convert back to tuple
"""
x=("apple","mango")
print("old x id:",id(x))
y=list(x)
y.append("banana")
print(y)
y[0]="ananas"
y.insert(1,"orange")
x=tuple(y)
del y
print(x)
print("new x id:",id(x))
t=(5,4,3,2,6,7)
print("old tuple id:",id(t))
  ##  tupl.sort()  not works because tuple is immutable
l=[5,6,8,1,2]
l.sort()
print("sorted list using l.sort() list:",l)
t=sorted(t)
print("new tuple id with same name:",id(t))
print("new sorted tuple using x=sorted(tuplename):",s_tuple)

print()

list1=[3,4,56,901,2]
print("list1:",list1)
print("list id before modification:",id(list1))
list1.append(45)
list1.extend([2,3,6,45])
print(list1)
print("id of modified list:",id(list1))




