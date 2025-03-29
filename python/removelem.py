def work(nums, val):
    #i think that the one thing that I wass missing was the check for he same 

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    return k, nums
print(work([3,2,2,3], 3))

#this is how we do back swaps 