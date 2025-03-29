def work(strs):
    dic = {}

    for i in strs:
        cur = "".join(sorted(i))

        if cur not in dic:
            dic[cur] = [i]
        else:
            dic[cur].append(i)
    return list(dic.values())

print(work(["eat","tea","tan","ate","nat","bat"]))