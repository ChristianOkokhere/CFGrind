def work(arr, k, x):
    #this one uses bs 

    if len(arr) <= k:
        return arr
    l, r = 0, len(arr) -1 

    while r-l + 1 > k:
        if abs(arr[l] - x) > abs(arr[r]- x):
            l += 1
        else:
            r -=1 
    return arr[l:r+1]