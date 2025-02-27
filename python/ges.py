def work(n):

  l, r = 0, n-1

  while l <= r:
    mid = (l + r) //2 
    g = guess(mid)

    if g == 0:
      return mid
    elif g == 1:
      l = mid + 1
    else:
      r = mid - 1
    return l