sample=[32,12,54,11,12,89,43]
print("original:",sample)
element=sample.pop(4)
print("after removing 4th index value:",sample)
sample.insert(2,element)
print("after adding at 2nd pos:",sample)
sample.append(element)
print(sample)
sample.extend([5,6,7])
print(sample)
start=1
end=6

#print(sample[start,end]) error
index=slice(start,end,1)
print(sample[index])