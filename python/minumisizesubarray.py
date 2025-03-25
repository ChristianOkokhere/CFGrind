def work(target, nums):
    #deal with ties
    #deal with the the end, we will keep a pass and also a ret 

    ret = float('inf')
    l = 0
    curs = 0 

    for r in range(len(nums)):
        curs += nums[r]
        
        while curs >= target:
            ret = min(ret, (r-l) + 1)

            curs -= nums[l]
            l += 1
         
            

    return 0 if ret == float('inf') else ret

print(work(11, [1,2,3,4,5]))