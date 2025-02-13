def work(pos):
  ret = 0

  ret += abs(pos[0]- 3)
  ret += abs(pos[1]-3)
  
  return ret

#lets bringer home, consids 

r = 0
pos = [0,0]
for _ in range(5):
  #this is bc we know that we have 5 of them duuuhh
  row = list(map(int, input().split()))

  if 1 in row:
    pos[0] = r + 1
    pos[1] = row.index(1) + 1 #just find the thing
  r += 1
print(work(pos))