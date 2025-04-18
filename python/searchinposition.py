def work(nums, target):
  l,r = 0, len(nums)- 1

  while l <= r:
    mid = (l +r) //2 

    if nums[mid] == target:
      return mid
    
    elif nums[mid] > target:
      r = mid - 1

    else:
      l = mid + 1
  return l

nums = [1,3,5,6]
target = 7

print(work(nums, target))