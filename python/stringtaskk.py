def work(inp):
  ret = []
  vow = {'a','e','i','o','u','y'}
  for i in inp:
    if i.lower() not in vow:
      ret.append(".")
      ret.append(i.lower())
  return "".join(ret)
      
#look at the input
word = input()
# word = "aBAcAba"
print(work(word))