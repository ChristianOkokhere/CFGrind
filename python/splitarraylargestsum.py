def work(nums, k):
    l,r = max(nums), sum(nums)

    while l < r:
        mid = l + (r-l) // 2

        if canSplit(nums, k, mid):
            #we need to look in the other direction
            r = mid
        else:
            l = mid + 1
    return l

def canSplit(nums, k, mid):
    part = 1 # I think this has to start at one 
    curs = 0 #this is because we want to control when to change it
    for i in range(len(nums)):

        #if adding in the thing will put us over edge 
        if curs + nums[i] > mid:
            curs = nums[i]
            part += 1
        #if we can fit the numer in just do dat lamo
        else:
            curs += nums[i]
    return part <= k

print(work([1,2,3,4,5], 2))