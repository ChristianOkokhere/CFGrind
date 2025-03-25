def work(nums, k):
    #we can do this in one pass

    dic = {} #make sure that we are udpating the elems as we are looking at them because the ones that are not true are closer to the nedt possible ones
    for r in range(len(nums)):
        if nums[r] not in dic:
            dic[nums[r]] = r

        elif nums[r] in dic:
            if abs(dic[nums[r]] - r) <= k:
                return True
            #update the pointer
            dic[nums[r]] = r
    return False

print(work([1,2,3,1,2,3], 2))