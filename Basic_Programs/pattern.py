def pattern1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def pattern2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

pattern1(5)
pattern2(5)