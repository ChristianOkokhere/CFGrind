def work(prices):
    #ok the idea here is that we need to keep track of the min price that we have seen and our ret

    if len(prices) < 2:
        return 0
    minp = prices[0]
    maxp = 0 
    for price in prices[1:]:
        curp = price - minp

        maxp = max(curp, maxp)

        minp = min(price, minp)
    return maxp