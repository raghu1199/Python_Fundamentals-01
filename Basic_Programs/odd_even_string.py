def printodd_even(str1):
    print("original string:",str1)
    print("only odd index characters:")
    for i in range(1,len(str1),2):
        print("index[",i,"]:",str1[i])
    print("only even index charcaters:")
    for i in range(0,len(str1),2):
        print("index[",i,"]:",str1[i])

def first():
    n1=int(input("num1:"))
    n2=int(input("num2:"))
    product=n1*n2
    if product>1000:
        return print("product is >1000 so sum is:",n1+n2)
    else:
        return print("product is <1000 so multiplication is:",n1*n2)

printodd_even("WElcome raghu?")
first()
