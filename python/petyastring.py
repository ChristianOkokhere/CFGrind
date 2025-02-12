def work(s1, s2):  
  s1 = s1.lower()
  s2 = s2.lower()
  
  if s1 < s2:
      return -1
  elif s1 > s2:
      return 1
  else:
      return 0
s1 = input()

s2 = input()
print(work(s1,s2))
