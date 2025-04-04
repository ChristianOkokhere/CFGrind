def work(nums, target):
    l,r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r-l)//2
        if nums[l] <= target:
            if nums[l] <= target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid -1 
    return -1