def work(piles, h):
    l, r = 1, max(piles)
    ret = float('inf')

    while l <= r:
        mid = l + (r-l)//2

        cur = 0
        for i in piles:
            cur += (i + mid-1) //2 
        if cur <= h:
            ret = min(ret, cur)
            r = mid -1 
        else:
            l = mid + 1

    return ret