number=[1,2,3,4]
numtuple=('one','two','three','four','five')
res=zip(number,numtuple)
#print(list(res))
resultset=set(res)
print(resultset)

#unzipp
num,numstring=zip(*resultset)
print("num:",num)
print("numstring:",numstring)
