original=[11,45,8,11,24,56,4,7,34,8,89,90,11]
string="hello world"
num_count=dict()
str_count=dict()
for char in string:
    if(char in num_count):
        num_count[char]+=1
    else:
        num_count[char]=1

for i in string:
    if(i in str_count):
        str_count[i]+=1
    else:
        str_count[i]=1
print("original",original)
print(num_count)
print("string:",string)
print(str_count)
