def work(weights, days):
    l, r = max(weights), sum(weights)

    ret = float('inf')
    while l <= r:
        mid = l + (r-l) //2 

        cur = 0 
        cday = 1 # i think that we are starting witht only one day

        for i in range(len(weights)):
            if cur + weights[i] > mid:
                cday += 1
                cur = weights[i]
            
        if cday <= days:
            ret = min(ret, mid)
            r = mid -1 
        else:
            l = mid + 1
    return ret