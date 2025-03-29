def work(nums):
    n = len(nums) // 2
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        
        if dic[i] > n:
            return i
        dic[i] += 1
print(work([2,2,1,1,1,2,2]))


