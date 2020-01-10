
#age=int(input("enter age"))
"""
age=10
is_over_age=(age>=18)
is_under_age=(age<18)
is_twenty=(age==20)

print("is_overage:",is_over_age)
print("is_underage:",is_under_age)
print("is_twenty:",is_twenty)
print("0 in boolean:",bool(0))
print("empty string:",bool(""))
"""
x=10
print(id(x))
x=x+1
print(id(x))   #chnaged now
y=x   #assigns object ref also so both same now
print("x:",x,"y:",y,end=" ")
print()
print("is x nad y same?:",x is y)  #True
y=y+1
print("x:",x,"y:",y)
print("is x nad y same?:",x is y)    #False


x=5 & 3
print(x)
y= 5 | 3
print(y)

x=35 and 2
print(x)  # 2

y= 35 and 0
print(y)   #0

x= 35 or 2
print(x)  #35

y= 0 or 40
print(y)  #40









