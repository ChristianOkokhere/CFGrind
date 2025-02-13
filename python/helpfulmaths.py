def work(inp):
  #the thing that I am thinking is to split by the Plus operateor then sort and join with the pus operator

  work = "+".join(sorted(inp.split("+")))
  return work

n = input()
print(work(n))