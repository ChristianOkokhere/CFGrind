# from collections import deque
# def work(s):
#     #can i not just use a deque and then do the for while thing here 

#     col = deque()

#     l = 0 
#     ret = 0

#     for r in range(len(s)):
#         #check the thing
#         if s[r] in col:
#             #colapse the thing
#             while s[r] in col:
#                 col.popleft()
#                 l += 1
#         col.append(s[r])
#         ret = max((r-l) + 1, ret)

#         #add the thing
        


#     return ret

# print(work("pwwkew"))
from collections import defaultdict
def work(s):
    cs = set()
    l = 0 
    ret = 0

    for r in range(len(s)):
        while s[r] in cs:
            cs.remove(s[l])
            l +=1
        cs.add(s[r])
        ret = max(ret, (r-l)+1)

    return ret