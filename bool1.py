name=""
print(bool(name))    #false
surname="smith"

greeting=name or f"Mr.{surname}"
print(greeting)   #Mr.smith

greeting1=name and f"Mr.{surname}"
print(bool(greeting1))  #False without bool it prints->nothing (empty strings)

name="raghu"
surname="smith"

print("both string true with or:",end=" ")     #first true here "raghu"
greeting=name or f"Mr.{surname}"
print(greeting)   #Mr.smith

print("both string true with and:",end=" ")     #second true here "Mr smith"
greeting=name and f"Mr.{surname}"
print(greeting)   #Mr.smith




print(not True)
print(not False)

print("cmp or:",end="")
cmp=(15>18) or (17<20)
print(cmp)    #True

print("cmp and:",end="")
cmp=(15>18) and (17<20)
print(cmp)   #False

age= int(input("enter age:"))
side_job=False
print(age>18 and age<65 or side_job)




