def work(nums, target):
    dic  = {}

    for i in range(len(nums)):
        #check if the thing is in there 
        res = target - nums[i]

        if res in dic:
            return [i, dic[res]]
        else:
            dic[nums[i]] = i

print(work([3,2,4], 6))