def mysqrt(x):
  #I think this is where I will do an intiger dfs

  l,r = 0, x

  while l <= r:
    m = (l + r)//2
    print(m)

    if m * m == x:
      return m #i think in this place we can also just return the midpoint
    
    if m * m > x:
      r = m -1
    else:
      l = m + 1
#need to work on the rounding here oh no i think that the way that i deal with the division does this already
  return r
x = 8
print(mysqrt(x))