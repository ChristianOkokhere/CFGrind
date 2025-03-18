def work(nums):
    #note that we are looking for the min to be in the l pointer so we need to plan accordingly

    l, r = 0, len(nums) -1 

    while l < r:
        mid = l + (r-l) //2 

        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]

print(work([11,13,15,17]))