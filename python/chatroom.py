def work(inp):
  hello = ["h",'e','l','l','o']
  hp = 0
  i = 0
  while i < len(inp) and hp < len(hello):
    #do the comp
    if inp[i] == hello[hp]:
      hp += 1
    i += 1
  
  if hp == len(hello):
    return "YES"
  return "NO"

n = input()

print(work(n))