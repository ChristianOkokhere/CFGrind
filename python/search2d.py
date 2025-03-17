def work(matrix, target):
    row,col = len(matrix), len(matrix[0])

    l,r = 0, row-1
    while l <= r:
        mid = l + (r-l) //2 

        if matrix[mid][0] <= target <= matrix[mid][col-1]:
            #here we are starting to look for what we want 
            start, finish = 0, col-1
            while start <= finish:
                midd = start + (finish - start) //2 

                if matrix[mid][midd] == target:
                    return True
                elif matrix[mid][midd] < target:
                    start = midd+1 
                else:
                    finish = midd - 1
            return False
        elif target < matrix[mid][0]:
            r = mid -1 
        else:
            l = mid + 1

    return False