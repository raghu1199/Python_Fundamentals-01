def miss_nums(num):
    original=[x for x in range(num[0],num[-1]+1)]
    num_set=set(num)
    return list(num_set^set(original))

print(miss_nums([1,2,3,5,7,8,11,13]))
