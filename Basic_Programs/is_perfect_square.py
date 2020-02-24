def is_perfectSquare(num):
    x=num//2
    y=set([x])
    while x*x!=num:
        x=(x+num//x)//2
        if x in y:
            return False
        else:
            y.add(x)

    return True

print(is_perfectSquare(16))