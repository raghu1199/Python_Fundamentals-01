li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
chunksize=int(len(li)/3)
#print(chunksize)
start=0
end=chunksize
for i in range(1,4,1):
    indexes=slice(start,end,1)
    chunklist=li[indexes]
    #chunklist=li[start,end,1] gives error
    print("chunk no:",i," ",chunklist)
    start=end
    end=end+chunksize
    print("revresed chunklist:",list(reversed(chunklist)))