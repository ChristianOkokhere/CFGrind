def work(inp, n):
  ret = [0] * n #this is the final place

  for i in range(len(inp)):
    ret[inp[i]-1] = i + 1 #make sure that we are looking at the placement of the things we are looking at
  return ret 

n = int(input())
inp = list(map(int, input().split()))

ans = work(inp,n)

for i in range(len(ans)-1):
  print(ans[i])#this gets you the new line 
print(ans[-1])
  
