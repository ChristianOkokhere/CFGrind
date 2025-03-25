# def work(target, mt):
#     #I think for this one you just need to find out what half of the array you are on
#     if self.searchasc(mt, 0, self.find_peak(mt, 0, mt.len())) != -1:
#         return self.searchasc(mt, 0, self.find_peak(mt, 0, mt.len()))
#     else:
#         return self.searchdesc(mt, self.find_peak(mt,0, mt.len()), mt.arry()-1, target)

# def find_peak(self, mt, left, right):
#     #we are looking for the point where the left and the right parts are both equal
#     while left < right:
#         mid = left + (right - left) //2 
#         #if we are still going up 
#         if mt.get(mid) < mt.get(mid+1):
#             left = mid + 1
#         else:
#             right = mid
#     return left 

# def searchasc(self, mt, left, right, target):
#     while left <= right:
#         mid = left + (right - left) // 2
#         #write in the optimizaiton to cut down on the calls here
#         if mt.get(mid) == target:
#             return mid
#         elif mt.get(mid) > target:
#             right = mid -1
#         else:
#             left = mid + 1
#     return -1

# def searchdesc(self, mt, left, right, target):
#     while left <= right:
#         mid = left + (right - left) // 2
#         midval = mt.get(mid)

#         if midval == target:
#             return mid 
#         elif midval > target:
#             right = mid -1 
#         else:
#             left = mid + 1
#     return -1

