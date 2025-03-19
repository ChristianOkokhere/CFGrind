def work(nums, target):
    #hikey this is the same question as the last one
    #  lamo
    l, r = 0, len(nums)-1
    while l<= r: #this is because we are searching 
        mid = l + (r-l)//2

        if target == nums[mid]:
            return True

        if nums[l] == nums[mid]:
            l += 1
            continue
        #now we see what part of the things is rotated
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid -1 
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid -1 
        
    return False

print(work([1,0,1,1,1], 0))