def work(inp):
    # Find leftmost min and max indices
    mai = inp.index(max(inp))  # leftmost max
    mii = inp.index(min(inp))  # leftmost min
    
    # Calculate moves needed
    ret = mai + (len(inp) - 1 - mii)
    
    return ret

n = int(input())
arr = list(map(int, input().split()))
print(work(arr))