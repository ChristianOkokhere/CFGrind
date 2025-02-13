def work(inp):
  #check if lucky or div by 7, 4, or its lcm

  check = {7,4,28,47}
  #check for lucky
  inp = str(inp)
  if sum([0 if int(inp[x]) in (7,4) else 1 for x in range(len(inp))]) == 0:
    return "YES"
  else:
    for i in check:
      if int("".join(inp)) % i == 0:
        return "YES"
  return "NO"

inp = input()

print(work(inp))