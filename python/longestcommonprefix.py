def work(strs):

    #cant think of a fast way to do this, but the slow way is not bad 
    ret = ""
    for i in range(len(strs[0])+ 1):
        cur = strs[0][:i]
        print(cur, "this is cur")

        for j in strs:
            print(j[:i])
            if j[:i] != cur:
                return ret
        ret = cur
    return ret

print(work(["flower","flower","flower","flower"]))

#one other way to do this one is to check each char at a time 