def work(nums, k):
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    print(sorted(dic.items()))
    return [item[0] for item in sorted(dic.items(), key=lambda x:x[1], reverse=True)[:k]]
    
print(work([1,2,2,3,3], 2))

#this is a cool solution need to think about how to do this with the faster sol