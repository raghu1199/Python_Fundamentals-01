roll=[47,40,64,69,37,76,83,95,97]
sample={'raghu':47,'emma':69,'rahul':40,'json':54}
print("list:",roll)
print("dictionary:",sample)
roll1=[]
for item in roll:
    if item in sample.values():
        roll1.append(item)

print(roll1)
roll.clear()
print(roll)
for i in range(0,len(roll1)):
    roll.append(roll1[i])

del roll1
print(roll)
#roll[:]=[item for item in roll if item in sample.values()]

